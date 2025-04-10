def read_file():
    file=input('enter the filename to be read:')

    try:
        with open(file, 'r') as infile:
            contents=infile.read()
            print('File read successfully')

            modified_contents=contents.upper()

            output_file='modified' + file

            with open(output_file, 'w') as newfile:
                newfile.write(modified_contents)
                print(f"  Modified wontent written to '{output_file}' " )
    except FileNotFoundError:
        print(f"ERROR: The file '{file}'does not exist ")
    except Exception as e:
        print('An error occured')
