from fpdf import FPDF


def render(
        *,
        words_txt='words.txt',
        cols=3,
        rows=7,
        words_pdf='words.pdf'):

    cell_w = 210 / cols
    cell_h = 297 / rows

    with open(words_txt, 'r') as f:
        words = f.readlines()

    print(f'Loaded {len(words)} words from {words_txt}')

    pdf = FPDF()
    pdf.set_margin(0)
    pdf.set_font('helvetica', 'B', 16)

    for i, word in enumerate(words):
        if i % (rows * cols) == 0:
            pdf.add_page()

        eol = (i + 1) % cols == 0
        new_x = 'LMARGIN' if eol else 'RIGHT'
        new_y = 'NEXT' if eol else 'LAST'

        pdf.cell(
            cell_w,
            cell_h,
            word,
            new_x=new_x,
            new_y=new_y,
            align='C',
            border=1)

    pdf.output(words_pdf)

    print(f'Generated {words_pdf}')


if __name__ == '__main__':
    render()
