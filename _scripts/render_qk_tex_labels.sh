#!/usr/bin/env bash
set -euo pipefail

# Render TeX labels/equations to SVG for the offline geometric intuition figures.
# Usage:
#   bash _scripts/render_qk_tex_labels.sh

OUT_DIR="assets/img/posts/qk-bias-rope/tex"
TMP_DIR="/tmp/qk_tex_labels"
mkdir -p "$OUT_DIR" "$TMP_DIR"

render_one() {
  local name="$1"
  local expr="$2"
  local tex="$TMP_DIR/${name}.tex"

  cat > "$tex" <<EOF
\\documentclass[12pt]{article}
\\usepackage{amsmath,amssymb}
\\pagestyle{empty}
\\begin{document}
\\[
${expr}
\\]
\\end{document}
EOF

  latex -interaction=nonstopmode -halt-on-error -output-directory "$TMP_DIR" "$tex" >/dev/null
  dvisvgm --no-fonts -n -o "${OUT_DIR}/${name}.svg" "${TMP_DIR}/${name}.dvi" >/dev/null
}

render_one x_r3 "x \\in \\mathbb{R}^3"
render_one y0_px_r2 "y_0 = Px \\in \\mathbb{R}^2"
render_one yA_bias "y_A = Px + \\alpha b"
render_one xprime "x' = x + \\alpha c"
render_one yB_bias "y_B = P(x+\\alpha c)"
render_one y_eq "y_A = y_B"
render_one eq_bias "c=P^{\\dagger}b,\\; y_A=Px+\\alpha b,\\; y_B=P(x+\\alpha c),\\; \\|y_A-y_B\\|_2"

render_one r3_theta_x "R_3x"
render_one yA_rope "y_A=P\\,R_3x"
render_one px_only "Px"
render_one yB_rope "y_B=R_2Px"
render_one eq_rope "y_A=P\\,R_3x,\\; y_B=R_2Px,\\; \\|y_A-y_B\\|_2"

echo "Rendered labels to ${OUT_DIR}"
