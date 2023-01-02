//
// File: file-bitsets.c
// Description: Encode strings or the contents of a file as a bitset.
//
// @author Kevin Wu, kw3705@rit.edu
//

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>

#define SET_SIZE 64
#define MAXLINE 256

/// Encode a given string as a bitset.
///
/// @param st is a character array to encode
/// @return the encoded string
uint64_t set_encode(char *st) {
    //printf("%s\n", st);
    uint64_t set = 0x0000000000000000;
    char *compare = "0123456789.abcdefghijklmnopqrstuvwxyz,ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    for(int i = 0; i < strlen(st); i++) {
        for(int j = 0; j < strlen(compare); j++) {
            if(st[i] == compare[j]) {
                switch(j) {
                    case 0: set = set | 0x8000000000000000;
                        break;
                    case 1: set = set | 0x4000000000000000;
                        break;
                    case 2: set = set | 0x2000000000000000;
                        break;
                    case 3: set = set | 0x1000000000000000;
                        break;
                    case 4: set = set | 0x0800000000000000;
                        break;
                    case 5: set = set | 0x0400000000000000;
                        break;
                    case 6: set = set | 0x0200000000000000;
                        break;
                    case 7: set = set | 0x0100000000000000;
                        break;
                    case 8: set = set | 0x0080000000000000;
                        break;
                    case 9: set = set | 0x0040000000000000;
                        break;
                    case 10: set = set | 0x0020000000000000;
                        break;
                    case 11: set = set | 0x0010000000000000;
                        break;
                    case 12: set = set | 0x0008000000000000;
                        break;
                    case 13: set = set | 0x0004000000000000;
                        break;
                    case 14: set = set | 0x0002000000000000;
                        break;
                    case 15: set = set | 0x0001000000000000;
                        break;
                    case 16: set = set | 0x0000800000000000;
                        break;
                    case 17: set = set | 0x0000400000000000;
                        break;
                    case 18: set = set | 0x0000200000000000;
                        break;
                    case 19: set = set | 0x0000100000000000;
                        break;
                    case 20: set = set | 0x0000080000000000;
                        break;
                    case 21: set = set | 0x0000040000000000;
                        break;
                    case 22: set = set | 0x0000020000000000;
                        break;
                    case 23: set = set | 0x0000010000000000;
                        break;
                    case 24: set = set | 0x0000008000000000;
                        break;
                    case 25: set = set | 0x0000004000000000;
                        break;
                    case 26: set = set | 0x0000002000000000;
                        break;
                    case 27: set = set | 0x0000001000000000;
                        break;
                    case 28: set = set | 0x0000000800000000;
                        break;
                    case 29: set = set | 0x0000000400000000;
                        break;
                    case 30: set = set | 0x0000000200000000;
                        break;
                    case 31: set = set | 0x0000000100000000;
                        break;
                    case 32: set = set | 0x0000000080000000;
                        break;
                    case 33: set = set | 0x0000000040000000;
                        break;
                    case 34: set = set | 0x0000000020000000;
                        break;
                    case 35: set = set | 0x0000000010000000;
                        break;
                    case 36: set = set | 0x0000000008000000;
                        break;
                    case 37: set = set | 0x0000000004000000;
                        break;
                    case 38: set = set | 0x0000000002000000;
                        break;
                    case 39: set = set | 0x0000000001000000;
                        break;
                    case 40: set = set | 0x0000000000800000;
                        break;
                    case 41: set = set | 0x0000000000400000;
                        break;
                    case 42: set = set | 0x0000000000200000;
                        break;
                    case 43: set = set | 0x0000000000100000;
                        break;
                    case 44: set = set | 0x0000000000080000;
                        break;
                    case 45: set = set | 0x0000000000040000;
                        break;
                    case 46: set = set | 0x0000000000020000;
                        break;
                    case 47: set = set | 0x0000000000010000;
                        break;
                    case 48: set = set | 0x0000000000008000;
                        break;
                    case 49: set = set | 0x0000000000004000;
                        break;
                    case 50: set = set | 0x0000000000002000;
                        break;
                    case 51: set = set | 0x0000000000001000;
                        break;
                    case 52: set = set | 0x0000000000000800;
                        break;
                    case 53: set = set | 0x0000000000000400;
                        break;
                    case 54: set = set | 0x0000000000000200;
                        break;
                    case 55: set = set | 0x0000000000000100;
                        break;
                    case 56: set = set | 0x0000000000000080;
                        break;
                    case 57: set = set | 0x0000000000000040;
                        break;
                    case 58: set = set | 0x0000000000000020;
                        break;
                    case 59: set = set | 0x0000000000000010;
                        break;
                    case 60: set = set | 0x0000000000000008;
                        break;
                    case 61: set = set | 0x0000000000000004;
                        break;
                    case 62: set = set | 0x0000000000000002;
                        break;
                    case 63: set = set | 0x0000000000000001;
                        break;
                    default: set = set | 0x0000000000000000;
                }
            }
        }
    }
    return(set);
}

/// Encode the contents of a file as a bitset.
///
/// @param fp is the file to read
/// @return the encoded file contents
uint64_t file_set_encode(FILE *fp) {
    uint64_t set = 0x0000000000000000;
    char buf[MAXLINE];
    size_t len = 0;
    while(fgets(buf, MAXLINE, fp) != NULL) {
        int loop = 1;
        for(int i = 0; i < len; i++) {
            if(buf[i] == EOF) {
                loop = 0;
                break;
            }
        }
        set = set | set_encode(buf);
        if(loop == 0) {
            break;
        } 
    }
    return(set);
}

/// Find the intersection of two bitsets.
///
/// @param set1 is the first set
/// @param set2 is the second set
/// @return the intersection of the sets
uint64_t set_intersect( uint64_t set1, uint64_t set2 ) {
    uint64_t set = set1 & set2;
    return(set);
}

/// Find the union of the two bitsets.
///
/// @param set1 is the first set
/// @param set2 is the second set
/// @return the union of the sets
uint64_t set_union( uint64_t set1, uint64_t set2 ) {
    uint64_t set = set1 | set2;
    return(set);
}

/// Find the complement of a given bitset.
///
/// @param set1 is the given set
/// @return the complement of the given set
uint64_t set_complement( uint64_t set1 ) {
    uint64_t set = ~set1;
    return(set);
}

/// Subtract bitset set2 from bitset set1.
///
/// @param set1 is the first set
/// @param set2 is the set to remove from the first set
/// @return set1 without the values of set2
uint64_t set_difference( uint64_t set1, uint64_t set2 ) {
    uint64_t set = set1;
    set = (set1 | set2) ^ set2; 
    return(set);
}

/// Find the set of values not shared between the two bitsets.
///
/// @param set1 is the first bitset
/// @param set2 is the second bitset
/// @return the set of values not shared between the two given sets
uint64_t set_symdifference( uint64_t set1, uint64_t set2 ) {
    uint64_t set = set1 ^ set2;
    return(set);
}

/// Find decode the characters which made up a bitset.
///
/// @param is the given set
/// @return an array of the composition characters
char * set_decode( uint64_t set ) {
    char *compare = "0123456789.abcdefghijklmnopqrstuvwxyz,ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    char *members;
    members = (char *) calloc(64, sizeof(char));
    int curr_index = 0;
    uint64_t mask = 0x8000000000000000;
    for(int i = 0; i < SET_SIZE; i++) {
        if(set & mask) {
            members[curr_index] = compare[i];
            curr_index++;
        }
        mask = mask >> 1;
    }
    return(members);
}

/// Find the cardinality of the given set.
///
/// @param set is the given set
/// @return the cardinality of the set
size_t set_cardinality( uint64_t set ) {
    char *curr_set_decode;
    curr_set_decode = set_decode(set);
    size_t set_len = strlen(curr_set_decode);
    free(curr_set_decode);
    return(set_len);
}

/// Main function calls the supporting functions and prints the computations between two given strings or files.
///
/// @param argc is the argument count
/// @param argv are the command line arguments
/// @return 0 on success
int main(int argc, char *argv[]) {
    if(argc != 3) {
        printf("Usage: file-bitsets string1 string2\n");
    }
    else {
        // store if the string is a file
        int set1_file = 0;
        int set2_file = 0;

        // try to open set1 as file, else encode as string
        uint64_t set1;
        FILE *in1;
        in1 = fopen(argv[1], "r");
        if(in1 == NULL) {
            set1 = set_encode(argv[1]);
        }
        else {
            set1_file = 1;
            set1 = file_set_encode(in1);
            fclose(in1);
        }

        // try to open set2 as file, else encode as string
        uint64_t set2;
        FILE *in2;
        in2 = fopen(argv[2], "r");
        if(in2 == NULL) {
            set2 = set_encode(argv[2]);
        }
        else {
            set2_file = 1;
            set2 = file_set_encode(in2);
            fclose(in2);
        }
        
        // decode bitsets
        char *set1_decode = set_decode(set1);
        char *set2_decode = set_decode(set2);
        
        // print outputs
        if(set1_file == 1) {
            printf("string1:\t%s\tEncoding the file:\t%s\n", argv[1], argv[1]);
        }
        else {
            printf("string1:\t%s\tEncoding the string:\t%s\n", argv[1], argv[1]);
        }
        if(set2_file == 1) {
            printf("string2:\t%s\tEncoding the file:\t%s\n", argv[2], argv[2]);
        }
        else {
            printf("string2:\t%s\tEncoding the string:\t%s\n", argv[2], argv[2]);
        }
        printf("\n");
        printf("set1:\t0x%016lx\n", set1);
        printf("set2:\t0x%016lx\n", set2);
        printf("\n");
        printf("set_intersect:\t0x%016lx\n", set_intersect(set1, set2));
        printf("set_union:\t0x%016lx\n", set_union(set1, set2));
        printf("\n");
        printf("set1 set_complement:\t0x%016lx\n", set_complement(set1));
        printf("set2 set_complement:\t0x%016lx\n", set_complement(set2));
        printf("\n");
        printf("set_difference:\t\t0x%016lx\n", set_difference(set1, set2));
        printf("set_symdifference:\t0x%016lx\n", set_symdifference(set1, set2));
        printf("\n");
        printf("set1 set_cardinality:\t%ld\n", set_cardinality(set1));
        printf("set2 set_cardinality:\t%ld\n", set_cardinality(set2));
        printf("\n");
        printf("members of set1:\t'%s'\n", set1_decode);
        printf("members of set2:\t'%s'\n", set2_decode);

        // free memory
        free(set1_decode);
        free(set2_decode);
    }
    return(0);
}
