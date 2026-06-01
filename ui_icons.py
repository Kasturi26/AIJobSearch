"""Inline SVG icons — work without external CDN in Streamlit."""


def icon(name: str, size: int = 28, color: str = "currentColor") -> str:
    s = str(size)
    c = color
    icons = {
        "sparkles": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2" stroke-linecap="round"><path d="M12 3l1.5 4.5L18 9l-4.5 1.5L12 15l-1.5-4.5L6 9l4.5-1.5L12 3z"/><path d="M5 19l1 3 1-3 3-1-3-1-1-3-1 3-3 1 3 1 1 3z"/><path d="M19 13l.5 1.5 1.5.5-1.5.5-.5 1.5-.5-1.5L17 15l1.5-.5.5-1.5z"/></svg>',
        "file": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6M8 13h8M8 17h5"/></svg>',
        "checklist": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg>',
        "robot": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><rect x="4" y="8" width="16" height="12" rx="2"/><path d="M9 8V6a3 3 0 116 0v2M12 14v2M8 14h.01M16 14h.01"/></svg>',
        "briefcase": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2"/></svg>',
        "target": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg>',
        "chart": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M3 3v18h18"/><path d="M7 16l4-6 4 3 5-8"/></svg>',
        "bolt": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>',
        "upload": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4M17 8l-5-5-5 5M12 3v12"/></svg>',
        "cpu": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><rect x="4" y="4" width="16" height="16" rx="2"/><path d="M9 1v3M15 1v3M9 20v3M15 20v3M1 9h3M1 15h3M20 9h3M20 15h3"/></svg>',
        "insights": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M12 2v4M12 18v4M4.93 4.93l2.83 2.83M16.24 16.24l2.83 2.83M2 12h4M18 12h4M4.93 19.07l2.83-2.83M16.24 7.76l2.83-2.83"/><circle cx="12" cy="12" r="4"/></svg>',
        "jobs": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M3 21h18M5 21V7l8-4v18M19 21V11l-6-3"/><path d="M9 9v.01M9 12v.01M9 15v.01"/></svg>',
        "pdf": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6"/><path d="M10 12h4M10 16h2"/></svg>',
        "shield": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
        "search": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><circle cx="11" cy="11" r="8"/><path d="M21 21l-4.35-4.35"/></svg>',
        "user": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M20 21v-2a4 4 0 00-4-4H8a4 4 0 00-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
        "trend": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M23 6l-9.5 9.5-5-5L1 18"/><path d="M17 6h6v6"/></svg>',
        "tag": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M20.59 13.41l-7.17 7.17a2 2 0 01-2.83 0L2 12V2h10l8.59 8.59a2 2 0 010 2.82z"/><circle cx="7" cy="7" r="1.5" fill="{c}"/></svg>',
        "star": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="{c}" stroke="{c}" stroke-width="1"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>',
        "pin": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 1118 0z"/><circle cx="12" cy="10" r="3"/></svg>',
        "clock": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>',
        "check": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2.5"><path d="M20 6L9 17l-5-5"/></svg>',
        "building": f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="{c}" stroke-width="2"><path d="M3 21h18M9 21V7l6-3v17M9 9h.01M15 9h.01M9 13h.01M15 13h.01"/></svg>',
    }
    return icons.get(name, "")


def stat_card(ic: str, ic_bg: str, ic_color: str, value: str, label: str) -> str:
    return f"""
    <div style="background:#fff;border:1px solid #e2e8f0;border-radius:14px;padding:16px 20px;
        display:flex;align-items:center;gap:14px;box-shadow:0 4px 16px rgba(15,23,42,0.06);min-height:80px;">
        <div style="width:48px;height:48px;border-radius:12px;background:{ic_bg};
            display:flex;align-items:center;justify-content:center;flex-shrink:0;color:{ic_color};">
            {icon(ic, 26, ic_color)}
        </div>
        <div>
            <div style="font-size:1.15rem;font-weight:800;color:#0f172a;line-height:1.2;">{value}</div>
            <div style="font-size:0.72rem;font-weight:600;color:#64748b;text-transform:uppercase;
                letter-spacing:0.05em;margin-top:2px;">{label}</div>
        </div>
    </div>"""


def feature_card(ic: str, ic_bg: str, ic_color: str, title: str, desc: str) -> str:
    return f"""
    <div style="background:#ffffff;border:1px solid #e2e8f0;border-radius:16px;padding:28px 20px;
        text-align:center;box-shadow:0 4px 20px rgba(15,23,42,0.06);min-height:175px;">
        <div style="width:60px;height:60px;margin:0 auto 14px;border-radius:16px;background:{ic_bg};
            display:flex;align-items:center;justify-content:center;color:{ic_color};">
            {icon(ic, 30, ic_color)}
        </div>
        <div style="font-size:1.05rem;font-weight:700;color:#0f172a;margin-bottom:6px;">{title}</div>
        <div style="font-size:0.88rem;color:#64748b;line-height:1.5;">{desc}</div>
    </div>"""


def process_step(num: int, ic: str, title: str, desc: str, accent: str) -> str:
    return f"""
    <div style="background:#fff;border:1px solid #e2e8f0;border-radius:16px;padding:22px 16px;
        text-align:center;box-shadow:0 4px 16px rgba(15,23,42,0.05);position:relative;margin-top:8px;">
        <div style="position:absolute;top:-14px;left:50%;transform:translateX(-50%);
            width:28px;height:28px;background:linear-gradient(135deg,{accent},#0891b2);
            border-radius:50%;color:#fff;font-size:0.75rem;font-weight:800;
            display:flex;align-items:center;justify-content:center;border:3px solid #f0f4f8;">{num}</div>
        <div style="width:56px;height:56px;margin:12px auto 14px;border-radius:50%;
            background:linear-gradient(145deg,{accent}22,{accent}11);
            display:flex;align-items:center;justify-content:center;color:{accent};">
            {icon(ic, 28, accent)}
        </div>
        <div style="font-size:0.95rem;font-weight:700;color:#0f172a;margin-bottom:6px;">{title}</div>
        <div style="font-size:0.8rem;color:#64748b;line-height:1.45;">{desc}</div>
    </div>"""


def upload_hero_header() -> str:
    """Top of the upload card — icons and copy."""
    return f"""
    <div style="text-align:center;padding-bottom:0.5rem;">
        <div style="width:80px;height:80px;margin:0 auto 1rem;border-radius:22px;
            background:linear-gradient(145deg,#dbeafe,#e0f2fe);
            display:flex;align-items:center;justify-content:center;
            box-shadow:0 8px 24px rgba(37,99,235,0.15);color:#2563eb;">
            {icon("upload", 38, "#2563eb")}
        </div>
        <div style="font-size:1.35rem;font-weight:800;color:#0f172a;letter-spacing:-0.02em;margin-bottom:0.35rem;">
            Drop your resume here
        </div>
        <div style="font-size:0.92rem;color:#64748b;margin-bottom:1rem;">
            or use the browse button below
        </div>
        <div style="display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin-bottom:0.25rem;">
            <span style="display:inline-flex;align-items:center;gap:5px;background:#eff6ff;color:#1d4ed8;
                font-size:0.75rem;font-weight:600;padding:6px 12px;border-radius:999px;border:1px solid #bfdbfe;">
                {icon("pdf", 12, "#2563eb")} PDF only
            </span>
            <span style="display:inline-flex;align-items:center;gap:5px;background:#f0fdf4;color:#047857;
                font-size:0.75rem;font-weight:600;padding:6px 12px;border-radius:999px;border:1px solid #bbf7d0;">
                {icon("robot", 12, "#059669")} AI analysis
            </span>
            <span style="display:inline-flex;align-items:center;gap:5px;background:#f8fafc;color:#475569;
                font-size:0.75rem;font-weight:600;padding:6px 12px;border-radius:999px;border:1px solid #e2e8f0;">
                {icon("shield", 12, "#475569")} Secure & private
            </span>
        </div>
    </div>"""
