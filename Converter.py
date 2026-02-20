def convert_conjugations(input_file):
    with open(input_file, 'r', encoding="UTF-8") as file:
        lines = [line.rstrip("\n") for line in file]

    output_lines = []
    i = 0

    while i < len(lines):
        line = lines[i].strip()
        if not line:
            i += 1
            continue

        verb = line
        i += 1

        if i >= len(lines):
            break

        i += 1

        while i < len(lines) and not lines[i].strip():
            i += 1

        if i < len(lines) and "POSITIVE" in lines[i].upper() and "NEGATIVE" in lines[i].upper():
            i += 1

        forms = {
            "tú": ["", ""],
            "usted": ["", ""],
            "nosotros": ["", ""],
            "ustedes": ["", ""],
        }

        while i < len(lines):
            row = lines[i].strip()
            if not row:
                i += 1
                break

            parts = row.split("\t")
            if len(parts) >= 3:
                pronoun = parts[0].strip()
                positive = parts[1].strip()
                negative = parts[2].strip()
                if pronoun in forms:
                    forms[pronoun] = [positive, negative]

            i += 1

        output_lines.append(verb)
        output_lines.append(forms["tú"][0])
        output_lines.append(forms["tú"][1])
        output_lines.append(forms["usted"][0])
        output_lines.append(forms["usted"][1])
        output_lines.append(forms["nosotros"][0])
        output_lines.append(forms["nosotros"][1])
        output_lines.append(forms["ustedes"][0])
        output_lines.append(forms["ustedes"][1])

    return output_lines

def write_output(output_file, output_lines):
    with open(output_file, 'w', encoding='UTF-8') as file:
        for line in output_lines:
            file.write(line + '\n')

if __name__ == "__main__":
    input_file = "new_whatever_format.txt"
    output_file = "asdfghjkl.txt"

    output_lines = convert_conjugations(input_file)
    write_output(output_file, output_lines)
    print("Conversion completed. Output saved to", output_file)
