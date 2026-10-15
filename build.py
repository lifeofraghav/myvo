#!/usr/bin/env python3
"""Inject img/*.jpg as base64 data URIs into kalpa_tpl3.html -> kalpa.html"""
import base64, pathlib

root = pathlib.Path(__file__).parent
MAP = {
    "__HERO__": "myvo_hero.jpg",
    "__SYSTEM__": "myvo_system.jpg",
    "__BOX__": "myvo_box.jpg",
    "__POUCHW__": "myvo_pouch_wide.jpg",
    "__FLOAT__": "myvo_float_cut.webp",
    "__JAR__": "c_jar.jpg",
    "__SEEDS__": "c_micro.jpg",
    "__ORCHARD__": "c_labwide.jpg",
    "__RUNNER__": "c_runner.jpg",
    "__LAB__": "c_lab.jpg",
    "__JARMACRO__": "c_jarm.jpg",
    "__POUCH__": "c_pouch.jpg",
    "__CARTON__": "c_carton.jpg",
    "__TRIO__": "c_trio.jpg",
    "__FLOORL__": "c_floor_land.jpg",
    "__FLOORP__": "c_floor_port.jpg",
}
html = (root / "kalpa_tpl3.html").read_text(encoding="utf-8")
for token, fname in MAP.items():
    data = base64.b64encode((root / "img" / fname).read_bytes()).decode()
    mime = {"png": "image/png", "webp": "image/webp"}.get(fname.rsplit(".", 1)[-1], "image/jpeg")
    html = html.replace(token, f"data:{mime};base64,{data}")
out = root / "kalpa.html"
out.write_text(html, encoding="utf-8")
print(f"built {out} ({out.stat().st_size/1e6:.2f} MB)")
