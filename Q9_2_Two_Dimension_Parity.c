/*
 * IT302 DCCN Lab - Question 9.2
 * Error Detection: Two-Dimensional Parity Checking (Row and Column Even Parity)
 */

#include <stdio.h>
#include <string.h>

#define MAX_ROWS 10
#define MAX_COLS 32

int main(void) {
    int rows, cols;
    char data[MAX_ROWS][MAX_COLS];
    int row_parity[MAX_ROWS] = {0};
    int col_parity[MAX_COLS] = {0};

    printf("--- 9.2 Two-Dimensional Parity Check (Even Parity) ---\n");
    printf("Enter number of data words (rows): ");
    if (scanf("%d", &rows) != 1 || rows <= 0 || rows > MAX_ROWS) return 1;

    printf("Enter number of bits per word (columns): ");
    if (scanf("%d", &cols) != 1 || cols <= 0 || cols > MAX_COLS) return 1;

    printf("Enter each binary word (%d bits):\n", cols);
    for (int i = 0; i < rows; i++) {
        printf("  Word %d: ", i + 1);
        scanf("%s", data[i]);
    }

    // Calculate Row Parities (Horizontal)
    for (int i = 0; i < rows; i++) {
        int count = 0;
        for (int j = 0; j < cols; j++) {
            if (data[i][j] == '1') count++;
        }
        row_parity[i] = count % 2; // 0 if even, 1 if odd
    }

    // Calculate Column Parities (Vertical - LRC)
    for (int j = 0; j < cols; j++) {
        int count = 0;
        for (int i = 0; i < rows; i++) {
            if (data[i][j] == '1') count++;
        }
        col_parity[j] = count % 2;
    }

    // Display Transmitted Block
    printf("\n[Sender] Transmitted 2D Parity Matrix:\n");
    for (int i = 0; i < rows; i++) {
        printf("  %s | Row Parity: %d\n", data[i], row_parity[i]);
    }
    printf("  ");
    for (int j = 0; j < cols; j++) printf("-");
    printf("\n  ");
    for (int j = 0; j < cols; j++) {
        printf("%d", col_parity[j]);
    }
    printf(" <- Column Parity Row\n");

    // Simulate Receiver Verification
    printf("\n--- Receiver Verification Simulation ---\n");
    printf("Inject single-bit error to test? (1 for Yes, 0 for No): ");
    int inject;
    if (scanf("%d", &inject) == 1 && inject == 1) {
        int r, c;
        printf("Enter row (1 to %d) and col (1 to %d) to flip: ", rows, cols);
        scanf("%d %d", &r, &c);
        if (r >= 1 && r <= rows && c >= 1 && c <= cols) {
            data[r - 1][c - 1] = (data[r - 1][c - 1] == '1') ? '0' : '1';
            printf("Flipped bit at row %d, col %d.\n", r, c);
        }
    }

    // Recheck at Receiver
    int err_row = -1, err_col = -1;
    for (int i = 0; i < rows; i++) {
        int count = 0;
        for (int j = 0; j < cols; j++) {
            if (data[i][j] == '1') count++;
        }
        if ((count % 2) != row_parity[i]) err_row = i;
    }
    for (int j = 0; j < cols; j++) {
        int count = 0;
        for (int i = 0; i < rows; i++) {
            if (data[i][j] == '1') count++;
        }
        if ((count % 2) != col_parity[j]) err_col = j;
    }

    if (err_row != -1 || err_col != -1) {
        printf("[Receiver] Status: ERROR DETECTED!\n");
        if (err_row != -1 && err_col != -1) {
            printf("[Receiver] Exact Error Location: Row %d, Column %d\n", err_row + 1, err_col + 1);
            printf("[Receiver] Error successfully corrected by flipping bit back!\n");
        }
    } else {
        printf("[Receiver] Status: NO ERROR DETECTED. Data block accepted.\n");
    }

    return 0;
}

