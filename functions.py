import pdfplumber
import re

import codecs


def convert(file_path=False):
    if not file_path:
        import tkinter as tk
        from tkinter import filedialog

        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(
            filetypes=[("PDFs", ".pdf")], title="Datei zum konvertieren auswählen!"
        )

    conv_string = []

    # open PDF
    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            crop = page.crop((60, 80, page.width, page.height))
            #     first_page = pdf.pages[0]
            # first_page = first_page.crop((60, 80, first_page.width, first_page.height))
            text = crop.extract_text(layout=True)
            no_trail = re.sub("\ +\\n", "\n", text)  # cleared trailing spaces
            no_wrong_nl = re.sub(
                "\\n\ +([A-Za-z0-9])", r" \1", no_trail
            )  # clear wrong newlins
            lines = re.split("\n", no_wrong_nl)  # split into lines

            test = 1
            changed_lines = []
            for line in lines:
                line, num = re.subn("(:)(.+)", rf"\1 {{{{c{test}::\2}}}}", line)
                if num > 0:
                    test += 1
                changed_lines.append(line)
            new_str = "\n".join(changed_lines).strip()
            conv_string.append(new_str)

    conv_string = "#################### neue Seite ####################\n".join(
        conv_string
    )

    file_path = file_path.replace(".pdf", ".txt")
    text_file = codecs.open(file_path, "w", "utf-8")
    text_file.write(conv_string)
    text_file.close()

    print(f"Alles fertig, die Datei befindet sich unter {file_path}")
    if not __name__ == "__main__":
        return conv_string


def convert_text(text):
    text = str(text)
    if "\r\n" in text:
        text = text.replace("\r\n", "\n")

    no_wrong_nl = re.sub("\\n\ +([A-Za-z0-9])", r" \1", text)  # clear wrong newlins
    lines = re.split("\n", no_wrong_nl)  # split into lines

    test = 1
    changed_lines = []
    for line in lines:
        line, num = re.subn("(:)(.+)", rf"\1 {{{{c{test}::\2}}}}", line)
        if num > 0:
            test += 1
        changed_lines.append(line)
    new_str = "\n".join(changed_lines).strip()
    if not __name__ == "__main__":
        return new_str


if __name__ == "__main__":
    convert()
