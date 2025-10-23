import argparse, json, shutil, re
from pathlib import Path

BASE = Path(__file__).resolve().parent
CONFIG = BASE / "config.json"
IMAGES = BASE / "static" / "images"

def load():
    return json.loads(CONFIG.read_text(encoding="utf-8"))

def save(cfg):
    CONFIG.write_text(json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8")
    print("✔ config.json обновлён")

def sanitize(name:str)->str:
    import re
    return re.sub(r'[^A-Za-z0-9_.-]+', '_', name)

def ensure_path(p:str)->str:
    p = p.strip()
    if p.startswith(("http://","https://")): return p
    src = Path(p).expanduser().resolve()
    if not src.exists(): raise FileNotFoundError(src)
    IMAGES.mkdir(parents=True, exist_ok=True)
    dst = IMAGES / sanitize(src.name)
    i=1
    while dst.exists():
        dst = IMAGES / f"{dst.stem}_{i}{dst.suffix}"; i+=1
    shutil.copyfile(src, dst)
    print(f"📦 {src} -> {dst}")
    return f"/static/images/{dst.name}"

def cmd_set_hero(args):
    cfg = load()
    cfg["heroImage"] = ensure_path(args.path)
    save(cfg)

def cmd_add_gallery(args):
    cfg = load(); cfg.setdefault("gallery", [])
    for p in args.paths:
        cfg["gallery"].append(ensure_path(p))
    save(cfg)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(required=True)
    p1 = sub.add_parser("set-hero"); p1.add_argument("path"); p1.set_defaults(func=cmd_set_hero)
    p2 = sub.add_parser("add-gallery"); p2.add_argument("paths", nargs="+"); p2.set_defaults(func=cmd_add_gallery)
    args = ap.parse_args(); args.func(args)