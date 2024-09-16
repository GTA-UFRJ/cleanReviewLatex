 OpenAI o1-preview
import sys
import re

def process_latex(content):
    output = ''
    i = 0  # Index to traverse the content
    length = len(content)

    while i < length:
        # Check for '\add{'
        if content[i:i+5] == '\\add{':
            i += 5  # Move index past '\add{'
            start = i
            brace_count = 1  # Initialize brace count for nested braces
            # Loop until the matching closing brace is found
            while i < length and brace_count > 0:
                if content[i] == '{':
                    brace_count += 1  # Found an opening brace
                elif content[i] == '}':
                    brace_count -= 1  # Found a closing brace
                i += 1
            # Extract the text inside '\add{...}'
            added_text = content[start:i-1]
            # Determine if we're inside a word
            prev_char = output[-1] if output else ''
            next_char = content[i] if i < length else ''
            inside_word = prev_char.isalnum() and next_char.isalnum()
            # Handle spaces based on context
            if not inside_word:
                # Between words: Ensure proper spacing
                if output and not output[-1].isspace() and added_text and not added_text[0].isspace():
                    if output[-1].isalnum() and added_text[0].isalnum():
                        output += ' '  # Add a space to separate words
            # Append the added text to the output
            output += added_text
        # Check for '\rem{'
        elif content[i:i+5] == '\\rem{':
            # Save the position before '\rem{'
            prev_char = output[-1] if output else ''
            prev_prev_char = output[-2] if len(output) >= 2 else ''
            # Determine if we're inside a word
            temp_i = i + 5
            brace_count = 1
            # Skip the content inside '\rem{...}'
            while temp_i < length and brace_count > 0:
                if content[temp_i] == '{':
                    brace_count += 1
                elif content[temp_i] == '}':
                    brace_count -= 1
                temp_i += 1
            next_char = content[temp_i] if temp_i < length else ''
            inside_word = prev_char.isalnum() and next_char.isalnum()
            # Advance index past '\rem{...}'
            i = temp_i
            # If we're not inside a word, handle spaces
            if not inside_word:
                # Check if we should remove the space before '\rem{...}'
                remove_space_before = False
                if output and output[-1].isspace():
                    # Only remove the space if the character before the space is alphanumeric
                    if prev_prev_char.isalnum():
                        remove_space_before = True
                # Remove the space before if necessary
                if remove_space_before:
                    output = output[:-1]
                # Skip any whitespace after '\rem{...}'
                while i < length and content[i].isspace():
                    i += 1
                # Add a space if needed
                if output and i < length:
                    if output[-1].isalnum() and content[i].isalnum():
                        output += ' '
            # If inside a word, do nothing (just skip the removed text)
        else:
            # Regular character, add it to output
            output += content[i]
            i += 1
    # Replace multiple spaces with a single space
    output = re.sub(' +', ' ', output)
    return output

if __name__ == '__main__':
    # Ensure the script is called with the correct number of arguments
    if len(sys.argv) != 3:
        print('Usage: python clean_latex.py input.tex output.tex')
        sys.exit(1)
    input_file = sys.argv[1]   # Input LaTeX file with '\add{}' and '\rem{}'
    output_file = sys.argv[2]  # Output LaTeX file without the commands
    # Read the content of the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Process the LaTeX content
    cleaned_content = process_latex(content)
    # Write the cleaned content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
