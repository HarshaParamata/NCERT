#include <stdio.h>

// Function to generate terms of the geometric progression and store in a file
void generate_GP_and_store(int initial_term, int common_ratio, int num_terms, const char* filename) {
    FILE *fp;
    fp = fopen(filename, "w");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return;
    }

    // Generate terms of the geometric progression
    int term = initial_term;
    fprintf(fp, "n\tTerm\n");
    for (int i = 0; i < num_terms; i++) {
        fprintf(fp, "%d\t%d\n", i, term);
        term *= common_ratio;
    }

    fclose(fp);
}

int main() {
    int initial_term = 1;
    int common_ratio = 3;
    int num_terms = 6;  // Number of terms to generate
    const char* filename = "gp_data1.txt";

    // Generate terms of the geometric progression and store in a file
    generate_GP_and_store(initial_term, common_ratio, num_terms, filename);

    printf("Data generated and stored in %s\n", filename);

    return 0;
}
