#!/usr/bin/env python3
"""
Xserver用ファイル生成スクリプト
吉岡さん方式に合わせた10個のフォルダ構成を生成
"""

import os
import shutil
from pathlib import Path

# 販売リンクの対応表
REDIRECT_URLS = {
    1: "https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi41q3pp22zj",
    2: "https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi41q33f45o4",
    3: "https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi41qhnrzmng",
    4: "https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi41q1o5alqr",
    5: "https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi6ud4gaywna",
    6: "https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi41q4mbpxi9",
    7: "https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi6fo2rk9rpd",
    8: "https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi6fo3bj5gfr",
    9: "https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi6fo3sxn5jm",
    10: "https://sf-system.jp/link.php?i=pi6fq1qhh6px&m=mi41q28cb1ef",
}

# 元のURLパターン
OLD_URL = "https://www.wellbest.jp/Landing/Formlp/rereje_rich_drta_amgif_2503com_up_after.aspx"

# 出力ディレクトリ
OUTPUT_DIR = Path("xserver-upload")

def main():
    print("=== Xserver用ファイル生成開始 ===\n")

    # 既存の出力ディレクトリを削除して再作成
    if OUTPUT_DIR.exists():
        shutil.rmtree(OUTPUT_DIR)
    OUTPUT_DIR.mkdir()

    # 共通リソースフォルダをコピー
    print("共通リソースをコピー中...")
    common_dir = OUTPUT_DIR / "rereje-rich78-common"
    common_dir.mkdir()

    for folder in ["assets", "manga", "products"]:
        if Path(folder).exists():
            shutil.copytree(folder, common_dir / folder)
            print(f"  ✓ {folder}/ をコピー")

    # index.htmlを読み込み
    with open("index.html", "r", encoding="utf-8") as f:
        original_html = f.read()

    # redirect-handler.jsの読み込み部分を削除（不要になる）
    html_template = original_html.replace(
        '<script src="assets/redirect-handler.js"></script>\n    ',
        ''
    )

    print("\n10個のフォルダを生成中...")

    # 10個のフォルダを生成
    for i in range(1, 11):
        folder_name = f"rereje-rich78-{i}"
        new_url = REDIRECT_URLS[i]

        print(f"[{i}/10] {folder_name} を生成中...")

        # フォルダ作成
        folder_path = OUTPUT_DIR / folder_name
        folder_path.mkdir()

        # HTMLを生成（販売リンクを書き換え）
        modified_html = html_template.replace(OLD_URL, new_url)

        # 共通リソースへの相対パスに変更
        modified_html = modified_html.replace('assets/', '../rereje-rich78-common/assets/')
        modified_html = modified_html.replace('manga/', '../rereje-rich78-common/manga/')
        modified_html = modified_html.replace('products/', '../rereje-rich78-common/products/')

        # ファイル保存
        output_file = folder_path / "index.html"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(modified_html)

        print(f"  ✓ {folder_name}/index.html 生成完了")
        print(f"     販売リンク: {new_url}")

    print("\n=== 生成完了 ===")
    print(f"出力先: {OUTPUT_DIR.absolute()}/\n")
    print("📂 フォルダ構成:")
    print(f"  ├── rereje-rich78-common/  (共通リソース)")
    print(f"  │   ├── assets/")
    print(f"  │   ├── manga/")
    print(f"  │   └── products/")
    for i in range(1, 11):
        print(f"  ├── rereje-rich78-{i}/")
        print(f"  │   └── index.html")

    print("\n次のステップ:")
    print("1. xserver-upload/ フォルダの中身をFTPでXserverにアップロード")
    print("2. アップロード先: public_html/")
    print("3. URL確認例:")
    print("   http://www.sf-ad.net/rereje-rich78-1")
    print("   http://www.sf-ad.net/rereje-rich78-2")
    print("   ...")
    print("   http://www.sf-ad.net/rereje-rich78-10")

if __name__ == "__main__":
    main()
