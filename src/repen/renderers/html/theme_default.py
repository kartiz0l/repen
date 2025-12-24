from typing import Dict

from repen.renderers.html.theme import HTMLTheme

CSS_RESET = """
*, *::before, *::after {
  box-sizing: border-box;
}

* {
  margin: 0;
}

@media (prefers-reduced-motion: no-preference) {
  html {
    interpolate-size: allow-keywords;
  }
}

body {
  line-height: 1.5;
  -webkit-font-smoothing: antialiased;
}

img, picture, video, canvas, svg {
  display: block;
  max-width: 100%;
}

input, button, textarea, select {
  font: inherit;
}

p, h1, h2, h3, h4, h5, h6 {
  overflow-wrap: break-word;
}

p {
  text-wrap: pretty;
}
h1, h2, h3, h4, h5, h6 {
  text-wrap: balance;
}

#root, #__next {
  isolation: isolate;
}
"""


class HTMLDefaultTheme(HTMLTheme):
    # Abstract methods implementation

    def variables(self) -> Dict[str, str]:
        return {
            # Base color
            "color-primary": "#2563eb",
            "color-primary-dark": "#1d4ed8",
            "color-secondary": "#64748b",
            "color-success": "#10b981",
            "color-warning": "#f59e0b",
            "color-danger": "#ef4444",
            # Text color
            "color-text": "#1f2937",
            "color-text-light": "#6b7280",
            "color-text-inverse": "#ffffff",
            # Background
            "color-bg": "#ffffff",
            "color-bg-secondary": "#f9fafb",
            "color-bg-tertiary": "#f3f4f6",
            # Border color
            "color-border": "#e5e7eb",
            "color-border-light": "#f3f4f6",
            # Spacing
            "spacing-xs": "0.25rem",
            "spacing-sm": "0.5rem",
            "spacing-md": "1rem",
            "spacing-lg": "1.5rem",
            "spacing-xl": "2rem",
            "spacing-2xl": "3rem",
            # Fonts
            "font-family-base": "-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif",
            "font-family-mono": "'SFMono-Regular', Consolas, 'Liberation Mono', Menlo, monospace",
            "font-size-base": "16px",
            "line-height-base": "1.6",
            # Layout
            "layout-max-width": "800px",
        }

    def styles(self) -> str:
        return f"""
{CSS_RESET}

body {{
    background-color: var(--color-bg);
    color: var(--color-text);
    font-family: var(--font-family-base);
    font-size: var(--font-size-base);
    line-height: var(--line-height-base);
    margin: 0;
    padding: 0;
}}

.layout {{
    width: 100%;
}}

.layout.vstack {{
    max-width: var(--layout-max-width);
    margin: 0 auto;
}}

.layout.vstack .item {{
    display: block;
}}

.bold {{
    font-weight: bold;
}}

.italic {{
    font-style: italic;
}}

.underline {{
    text-decoration: underline;
}}

.strikethrough {{
    text-decoration: line-through;
}}

.code {{
    font-family: var(--font-family-mono);
    //background: #ffeff0;
    //word-wrap: break-word;
    //box-decoration-break: clone;
    //padding: .1rem .3rem .2rem;
    //border-radius: .2rem;
}}
        """
