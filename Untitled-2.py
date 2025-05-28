def convert_conjugations(input_file):
    with open(input_file, 'r', encoding="UTF-8") as file:
        lines = file.readlines()
    asdf = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    output_lines = []
    temp = ""
    for line in lines:
        if "|" in line:
            output_lines.append(line.split(" | ")[1].strip())
            continue
        parts = line.split("\t")
        print(parts)
        if parts[0] == "yo":
            output_lines.append(parts[1])
            print("1")
            temp = parts[3]
        elif parts[0] == "tú":
            output_lines.append(parts[1])
            print("2")
        elif parts[0] == "usted":
            output_lines.append(parts[1])
            print("3")
            output_lines.append(temp.strip("\n"))
            output_lines.append(parts[3].strip("\n"))
            

    return output_lines

def write_output(output_file, output_lines):
    with open(output_file, 'w') as file:
        for line in output_lines:
            file.write(line + '\n')

if __name__ == "__main__":
    input_file = "whatever.txt"
    output_file = "asdfghjkl.txt"

    output_lines = convert_conjugations(input_file)
    write_output(output_file, output_lines)
    print("Conversion completed. Output saved to", output_file)
