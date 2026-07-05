// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-about",
    title: "about",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-blog",
          title: "blog",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/blog/";
          },
        },{id: "nav-publications",
          title: "publications",
          description: "publications in reversed chronological order.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/publications/";
          },
        },{id: "nav-projects",
          title: "projects",
          description: "Research directions and the code behind them.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-cv",
          title: "cv",
          description: "A full PDF version is also available.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/cv/";
          },
        },{id: "nav-teaching-amp-service",
          title: "teaching &amp; service",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/teaching-service/";
          },
        },{id: "post-handling-bias-and-rope-in-qk-attention-with-a-unified-geometric-view",
        
          title: "Handling Bias and RoPE in QK Attention with a Unified Geometric View",
        
        description: "A practical geometric view for analyzing QK circuits with bias and RoPE using a single bilinear form",
        section: "Posts",
        handler: () => {
          
            window.location.href = "/blog/2026/bias-and-rope-in-attention/";
          
        },
      },{id: "news-i-just-started-my-phd-in-computer-science-at-boston-university-advised-by-professor-mark-crovella",
          title: 'I just started my PhD in Computer Science at Boston University, advised by...',
          description: "",
          section: "News",},{id: "news-quot-dependence-and-model-selection-in-llp-the-problem-of-variants-quot-was-accepted-at-kdd-2023",
          title: '&amp;quot;Dependence and Model Selection in LLP: The Problem of Variants&amp;quot; was accepted at...',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/kdd23_paper/";
            },},{id: "news-new-preprint-quot-evaluating-llp-methods-challenges-and-approaches-quot",
          title: 'New preprint - &amp;quot;Evaluating LLP Methods: Challenges and Approaches.&amp;quot;',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/preprint_llp/";
            },},{id: "news-new-preprint-quot-sparse-attention-decomposition-applied-to-circuit-tracing-quot",
          title: 'New preprint - &amp;quot;Sparse Attention Decomposition Applied to Circuit Tracing.&amp;quot;',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/preprint_sparse_attention/";
            },},{id: "news-quot-disentangling-text-and-math-in-word-problems-quot-was-accepted-at-findings-of-acl-2025",
          title: '&amp;quot;Disentangling Text and Math in Word Problems&amp;quot; was accepted at Findings of ACL...',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/acl25_findings_paper/";
            },},{id: "news-quot-memscope-open-source-kernel-level-framework-for-heterogeneous-memory-characterization-quot-was-accepted-at-ieee-rtss-2025",
          title: '&amp;quot;MEMSCOPE: Open-Source Kernel-Level Framework for Heterogeneous Memory Characterization&amp;quot; was accepted at IEEE RTSS...',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/rtss25_paper/";
            },},{id: "news-invited-talk-at-bu-39-s-baaigl-lab",
          title: 'Invited talk at BU&amp;#39;s BAAIGL Lab.',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/talk_acc_baaigl_2025/";
            },},{id: "news-quot-pinpointing-attention-causal-communication-in-language-models-quot-was-accepted-at-neurips-2025",
          title: '&amp;quot;Pinpointing Attention-Causal Communication in Language Models&amp;quot; was accepted at NeurIPS 2025.',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/neurips25_paper/";
            },},{id: "news-invited-talks-at-brown-university-and-bu-39-s-tinlab",
          title: 'Invited talks at Brown University and BU&amp;#39;s TINLab.',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/talk_attention_first_principles/";
            },},{id: "news-invited-talk-at-universidade-federal-de-viçosa",
          title: 'Invited talk at Universidade Federal de Viçosa.',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/talk_ufv_2026/";
            },},{id: "news-quot-do-language-models-track-entities-across-state-changes-quot-was-accepted-at-icml-2026",
          title: '&amp;quot;Do Language Models Track Entities Across State Changes?&amp;quot; was accepted at ICML 2026....',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/icml26_entity_tracking/";
            },},{id: "news-quot-singular-vectors-of-attention-heads-align-with-features-quot-was-accepted-at-icml-2026",
          title: '&amp;quot;Singular Vectors of Attention Heads Align with Features&amp;quot; was accepted at ICML 2026....',
          description: "",
          section: "News",handler: () => {
              window.location.href = "/news/icml26_singular_vectors/";
            },},{id: "projects-why-attention-heads-attend-where-they-do",
          title: 'Why attention heads attend where they do',
          description: "Isolating the low-dimensional signals that cause attention, and using them to trace interpretable circuits from a single forward pass.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_attention_causal_communication/";
            },},{id: "projects-feature-geometry-in-attention-heads",
          title: 'Feature Geometry in Attention Heads',
          description: "When and why the singular vectors of attention matrices align with the features a model uses.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/2_feature_geometry/";
            },},{id: "projects-learning-from-label-proportions",
          title: 'Learning from Label Proportions',
          description: "Model selection and benchmarking for a weakly supervised setting where only bag-level label proportions are known.",
          section: "Projects",handler: () => {
              window.location.href = "/projects/3_learning_from_label_proportions/";
            },},{
        id: 'social-dblp',
        title: 'DBLP',
        section: 'Socials',
        handler: () => {
          window.open("https://dblp.org/pid/255/9604", "_blank");
        },
      },{
        id: 'social-email',
        title: 'email',
        section: 'Socials',
        handler: () => {
          window.open("mailto:%67%76%66%72%61%6E%63%6F@%62%75.%65%64%75", "_blank");
        },
      },{
        id: 'social-github',
        title: 'GitHub',
        section: 'Socials',
        handler: () => {
          window.open("https://github.com/gaabrielfranco", "_blank");
        },
      },{
        id: 'social-linkedin',
        title: 'LinkedIn',
        section: 'Socials',
        handler: () => {
          window.open("https://www.linkedin.com/in/gaabrielfranco", "_blank");
        },
      },{
        id: 'social-orcid',
        title: 'ORCID',
        section: 'Socials',
        handler: () => {
          window.open("https://orcid.org/0000-0003-0702-0146", "_blank");
        },
      },{
        id: 'social-rss',
        title: 'RSS Feed',
        section: 'Socials',
        handler: () => {
          window.open("/feed.xml", "_blank");
        },
      },{
        id: 'social-scholar',
        title: 'Google Scholar',
        section: 'Socials',
        handler: () => {
          window.open("https://scholar.google.com/citations?user=Ls46A88AAAAJ", "_blank");
        },
      },{
        id: 'social-x',
        title: 'X',
        section: 'Socials',
        handler: () => {
          window.open("https://twitter.com/gvsfranco", "_blank");
        },
      },{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
