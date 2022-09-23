#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    if len(argv[1:]) == 3:
        sign = {'+', '-', '*', '/'}
        if argv[2]  in sign:
            if type(int(argv[1])) == int and type(int(argv[3])) == int:
                print('done')
            else:
                print('error1')
                exit
        else:
            print('error2')
            exit
    else:
        print('error3')
        exit


    
    