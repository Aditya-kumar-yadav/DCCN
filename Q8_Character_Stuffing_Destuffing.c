/*
 * IT302 DCCN Lab - Question 8
 * Program to perform Character (Byte) Stuffing and De-stuffing.
 * Framing: Frame begins with "DLE STX" and ends with "DLE ETX".
 * Rule: Whenever "DLE" appears inside data, an extra "DLE" is stuffed.
 */

#include <stdio.h>
#include <string.h>

void char_stuff(const char *in, char *out) {
    int i = 0, j = 0;
    // Add Frame Header
    strcpy(out, "DLE STX ");
    j = (int)strlen(out);

    while (in[i] != '\0') {
        // Check for "DLE" token in data
        if (strncmp(&in[i], "DLE", 3) == 0 && (i == 0 || in[i-1] == ' ') && 
            (in[i+3] == ' ' || in[i+3] == '\0')) {
            strcpy(&out[j], "DLE DLE ");
            j += 8;
            i += 3;
            if (in[i] == ' ') i++;
        } else {
            out[j++] = in[i++];
        }
    }
    // Add Frame Trailer
    if (j > 0 && out[j-1] != ' ') out[j++] = ' ';
    strcpy(&out[j], "DLE ETX");
}

void char_destuff(const char *in, char *out) {
    int i = 0, j = 0;
    // Skip initial "DLE STX "
    if (strncmp(in, "DLE STX ", 8) == 0) {
        i = 8;
    }

    int len = (int)strlen(in);
    // Find where trailer " DLE ETX" begins
    int end_limit = len;
    if (len >= 8 && strcmp(&in[len - 8], " DLE ETX") == 0) {
        end_limit = len - 8;
    } else if (len >= 7 && strcmp(&in[len - 7], "DLE ETX") == 0) {
        end_limit = len - 7;
    }

    while (i < end_limit) {
        // If "DLE DLE" appears, destuff one "DLE"
        if (strncmp(&in[i], "DLE DLE", 7) == 0) {
            strcpy(&out[j], "DLE");
            j += 3;
            i += 7;
        } else {
            out[j++] = in[i++];
        }
    }
    // Trim trailing space if any
    while (j > 0 && out[j-1] == ' ') j--;
    out[j] = '\0';
}

int main(void) {
    char data[256], stuffed[512], destuffed[256];

    printf("Enter message string (e.g. NET DLE WORK): ");
    if (!fgets(data, sizeof(data), stdin)) return 1;
    data[strcspn(data, "\r\n")] = '\0'; // Remove newline

    char_stuff(data, stuffed);
    char_destuff(stuffed, destuffed);

    printf("\n--- Character Stuffing & De-stuffing Results ---\n");
    printf("Original Data   : %s\n", data);
    printf("Stuffed Frame   : %s\n", stuffed);
    printf("De-stuffed Data : %s\n", destuffed);
    printf("Integrity Match : %s\n", (strcmp(data, destuffed) == 0) ? "SUCCESS" : "FAILED");

    return 0;
}

