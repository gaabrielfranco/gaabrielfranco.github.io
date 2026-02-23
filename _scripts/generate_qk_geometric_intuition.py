#!/usr/bin/env python3
"""Generate a geometry-first intuition SVG for bias and RoPE equivalences.

No external dependencies required.
"""

from math import cos, sin


def add(a, b):
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def matvec(A, v):
    return (
        A[0][0] * v[0] + A[0][1] * v[1],
        A[1][0] * v[0] + A[1][1] * v[1],
    )


def transpose(A):
    return ((A[0][0], A[1][0]), (A[0][1], A[1][1]))


def matmul(A, B):
    return (
        (
            A[0][0] * B[0][0] + A[0][1] * B[1][0],
            A[0][0] * B[0][1] + A[0][1] * B[1][1],
        ),
        (
            A[1][0] * B[0][0] + A[1][1] * B[1][0],
            A[1][0] * B[0][1] + A[1][1] * B[1][1],
        ),
    )


def inv2(A):
    d = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return ((A[1][1] / d, -A[0][1] / d), (-A[1][0] / d, A[0][0] / d))


def rot(theta):
    c, s = cos(theta), sin(theta)
    return ((c, -s), (s, c))


def fmt(x):
    return f"{x:.2f}"


def plot_group(svg, x0, y0, w, h, title, subtitle, vectors, lim=2.0):
    # Background panel
    svg.append(
        f'<rect x="{x0}" y="{y0}" width="{w}" height="{h}" rx="14" fill="#ffffff" stroke="#d8d8d8" stroke-width="1.5"/>'
    )
    svg.append(f'<text x="{x0+16}" y="{y0+30}" class="panel-title">{title}</text>')
    svg.append(f'<text x="{x0+16}" y="{y0+52}" class="panel-sub">{subtitle}</text>')

    px0, py0 = x0 + 30, y0 + 70
    pw, ph = w - 60, h - 100

    # Grid and axes
    for i in range(-2, 3):
        gx = px0 + (i + lim) / (2 * lim) * pw
        gy = py0 + (lim - i) / (2 * lim) * ph
        svg.append(f'<line x1="{gx}" y1="{py0}" x2="{gx}" y2="{py0+ph}" class="grid"/>')
        svg.append(f'<line x1="{px0}" y1="{gy}" x2="{px0+pw}" y2="{gy}" class="grid"/>')

    xax_y = py0 + ph / 2
    yax_x = px0 + pw / 2
    svg.append(f'<line x1="{px0}" y1="{xax_y}" x2="{px0+pw}" y2="{xax_y}" class="axis"/>')
    svg.append(f'<line x1="{yax_x}" y1="{py0}" x2="{yax_x}" y2="{py0+ph}" class="axis"/>')

    def mappt(v):
        x = px0 + (v[0] + lim) / (2 * lim) * pw
        y = py0 + (lim - v[1]) / (2 * lim) * ph
        return x, y

    ox, oy = mappt((0.0, 0.0))

    # Draw vectors
    for v in vectors:
        tx, ty = mappt(v["to"])
        cls = v["cls"]
        svg.append(
            f'<line x1="{ox}" y1="{oy}" x2="{tx}" y2="{ty}" class="{cls}" marker-end="url(#arrow-{cls})"/>'
        )
        lx, ly = tx + 8, ty - 6
        svg.append(f'<text x="{lx}" y="{ly}" class="vec-label">{v["label"]}</text>')

    # Distance marker between the two path endpoints
    if len(vectors) >= 3:
        r_end = vectors[1]["to"]
        b_end = vectors[2]["to"]
        rx, ry = mappt(r_end)
        bx, by = mappt(b_end)
        svg.append(f'<line x1="{rx}" y1="{ry}" x2="{bx}" y2="{by}" class="eps"/>')


def main():
    # Well-conditioned-ish matrices
    Wq = ((1.10, 0.22), (-0.18, 0.95))
    Wk = ((0.92, -0.14), (0.26, 1.05))

    xd = (0.95, -0.55)
    xs = (-0.72, 0.88)

    bq = (0.36, -0.24)
    bk = (-0.29, 0.31)

    WqT = transpose(Wq)
    WkT = transpose(Wk)

    # Bias equivalence
    q_base = matvec(WqT, xd)
    k_base = matvec(WkT, xs)

    q_path_a = add(q_base, bq)  # project then translate
    k_path_a = add(k_base, bk)

    c_d = matvec(transpose(inv2(Wq)), bq)
    c_s = matvec(transpose(inv2(Wk)), bk)

    q_path_b = matvec(WqT, add(xd, c_d))  # translate then project
    k_path_b = matvec(WkT, add(xs, c_s))

    # RoPE equivalence
    Rd = rot(0.75)
    Rs = rot(-0.55)

    # Original: project then rotate in q/k space
    q_rope_a = matvec(transpose(Rd), q_base)
    k_rope_a = matvec(transpose(Rs), k_base)

    # Reformulation: rotate in residual space then project
    Md = matmul(matmul(Wq, Rd), inv2(Wq))
    Ms = matmul(matmul(Wk, Rs), inv2(Wk))
    q_rope_b = matvec(WqT, matvec(transpose(Md), xd))
    k_rope_b = matvec(WkT, matvec(transpose(Ms), xs))

    eps_bias_q = ((q_path_a[0] - q_path_b[0]) ** 2 + (q_path_a[1] - q_path_b[1]) ** 2) ** 0.5
    eps_bias_k = ((k_path_a[0] - k_path_b[0]) ** 2 + (k_path_a[1] - k_path_b[1]) ** 2) ** 0.5
    eps_rope_q = ((q_rope_a[0] - q_rope_b[0]) ** 2 + (q_rope_a[1] - q_rope_b[1]) ** 2) ** 0.5
    eps_rope_k = ((k_rope_a[0] - k_rope_b[0]) ** 2 + (k_rope_a[1] - k_rope_b[1]) ** 2) ** 0.5

    svg = []
    svg.append('<svg xmlns="http://www.w3.org/2000/svg" width="1500" height="980" viewBox="0 0 1500 980" role="img" aria-label="Geometric intuition for bias and RoPE equivalences">')
    svg.append('<rect x="0" y="0" width="1500" height="980" fill="#ffffff"/>')
    svg.append(
        """
<style>
.title { font: 700 34px Arial, sans-serif; fill: #111; }
.sub { font: 500 19px Arial, sans-serif; fill: #333; }
.row-title { font: 700 26px Arial, sans-serif; fill: #111; }
.panel-title { font: 700 20px Arial, sans-serif; fill: #1c1c1c; }
.panel-sub { font: 500 15px Arial, sans-serif; fill: #4a4a4a; }
.grid { stroke: #efefef; stroke-width: 1; }
.axis { stroke: #999; stroke-width: 1.8; }
.vec-base { stroke: #808080; stroke-width: 3; }
.vec-a { stroke: #d9544d; stroke-width: 3.6; }
.vec-b { stroke: #2f7fd1; stroke-width: 3.6; }
.vec-label { font: 500 14px Arial, sans-serif; fill: #222; }
.legend { font: 500 15px Arial, sans-serif; fill: #222; }
.eps { stroke: #222; stroke-width: 1.6; stroke-dasharray: 5 4; }
.note { font: 500 17px Arial, sans-serif; fill: #222; }
</style>
"""
    )

    # Arrow markers by class
    svg.append('<defs>')
    for cls, color in (("vec-base", "#808080"), ("vec-a", "#d9544d"), ("vec-b", "#2f7fd1")):
        svg.append(
            f'<marker id="arrow-{cls}" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><polygon points="0 0, 10 3, 0 6" fill="{color}"/></marker>'
        )
    svg.append('</defs>')

    svg.append('<text x="44" y="62" class="title">Geometric intuition: same endpoint through two paths</text>')
    svg.append('<text x="44" y="94" class="sub">Red path = original formulation. Blue path = ACC++ reformulation. Overlap means equivalence.</text>')

    svg.append('<text x="44" y="146" class="row-title">Bias: project then translate  vs  translate (via pseudoinverse pullback) then project</text>')

    plot_group(
        svg, 44, 170, 700, 350,
        "Query side",
        "q_A = W_Q^T x_d + b_Q  and  q_B = W_Q^T (x_d + c_d)",
        [
            {"to": q_base, "label": "W_Q^T x_d", "cls": "vec-base"},
            {"to": q_path_a, "label": "Path A", "cls": "vec-a"},
            {"to": q_path_b, "label": "Path B", "cls": "vec-b"},
        ],
    )
    plot_group(
        svg, 756, 170, 700, 350,
        "Key side",
        "k_A = W_K^T x_s + b_K  and  k_B = W_K^T (x_s + c_s)",
        [
            {"to": k_base, "label": "W_K^T x_s", "cls": "vec-base"},
            {"to": k_path_a, "label": "Path A", "cls": "vec-a"},
            {"to": k_path_b, "label": "Path B", "cls": "vec-b"},
        ],
    )

    svg.append('<text x="44" y="572" class="row-title">RoPE: project then rotate  vs  rotate in residual space then project</text>')

    plot_group(
        svg, 44, 596, 700, 350,
        "Query side",
        "q_A = R_d^T (W_Q^T x_d)  and  q_B = W_Q^T (M_d^T x_d)",
        [
            {"to": q_base, "label": "W_Q^T x_d", "cls": "vec-base"},
            {"to": q_rope_a, "label": "Path A", "cls": "vec-a"},
            {"to": q_rope_b, "label": "Path B", "cls": "vec-b"},
        ],
    )
    plot_group(
        svg, 756, 596, 700, 350,
        "Key side",
        "k_A = R_s^T (W_K^T x_s)  and  k_B = W_K^T (M_s^T x_s)",
        [
            {"to": k_base, "label": "W_K^T x_s", "cls": "vec-base"},
            {"to": k_rope_a, "label": "Path A", "cls": "vec-a"},
            {"to": k_rope_b, "label": "Path B", "cls": "vec-b"},
        ],
    )

    # Legend and assumptions
    svg.append('<rect x="1080" y="24" width="364" height="118" rx="10" fill="#f8f8f8" stroke="#d8d8d8"/>')
    svg.append('<line x1="1104" y1="58" x2="1158" y2="58" class="vec-base" marker-end="url(#arrow-vec-base)"/>')
    svg.append('<text x="1170" y="64" class="legend">Base projection</text>')
    svg.append('<line x1="1104" y1="86" x2="1158" y2="86" class="vec-a" marker-end="url(#arrow-vec-a)"/>')
    svg.append('<text x="1170" y="92" class="legend">Original path</text>')
    svg.append('<line x1="1104" y1="114" x2="1158" y2="114" class="vec-b" marker-end="url(#arrow-vec-b)"/>')
    svg.append('<text x="1170" y="120" class="legend">ACC++ path</text>')

    svg.append('<rect x="44" y="944" width="1412" height="26" fill="#ffffff"/>')
    svg.append(
        f'<text x="44" y="964" class="note">Endpoint gaps (small in this well-conditioned example): '
        f'bias-q={fmt(eps_bias_q)}, bias-k={fmt(eps_bias_k)}, rope-q={fmt(eps_rope_q)}, rope-k={fmt(eps_rope_k)}. '
        'Well-conditioned W_Q, W_K make pseudoinverse pullback numerically stable.</text>'
    )

    svg.append('</svg>')

    out = 'assets/img/posts/qk-bias-rope/geometric-path-equivalence.svg'
    with open(out, 'w', encoding='utf-8') as f:
        f.write('\n'.join(svg))
    print(f'Wrote {out}')


if __name__ == '__main__':
    main()
