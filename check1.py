import subprocess
import os

if not os.path.isfile("project1.py"):
    print("There is no project1.py file in this directory.")
    print("Exiting the test script.")
    exit()

prompts = [
    "Enter cards as <rank><suit> (e.g., AH or 10S).",  
    "Card 1:",
    "Card 2:",
    "Card 3:"
    ]

def clean_output(output):
    for prompt in prompts:
        output = output.replace(prompt, "")
    output = output.replace("\n", " ")
    output = output.replace("\r", " ")
    return output.strip()   

num_correct = 0

# Test cases 
input = [
    "1S\n5H\n2C\n",
    "JS\n5H\nJS\n",
    "2C\nJC\nKH\n",
    "JH\nQC\nKD\n",
    "3H\n2C\n6D\n"
    ]
expected = [
    "Invalid rank 1. Must be 2-10, J, Q, K, or A.", 
    "There can't be two JS in the same hand. You're playing with a fake deck!", 
    "Point value of hand: 12", 
    "Point value of hand: 10", 
    "Point value of hand: 6" 
    ]

for i in range(len(input)):
    input_data = input[i].strip()

    # Run project1.py with the given input
    result = subprocess.run(
        ["python", "project1.py"],
        input=input_data.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    # Decode the output from bytes to string and strip trailing whitespace
    output = result.stdout.decode().strip()
    output = clean_output(output)

    print("\n\n")
    print("Input was:", input_data.strip())
    print("Expected:", expected[i])
    print("Got:", output)

    # Compare and report
    if expected[i] == output:
        print("Output matches expected result.")
        num_correct += 1
    else:
        print("Output does NOT match.")

print(f"\n\n{num_correct} out of {len(input)} test cases passed.")
