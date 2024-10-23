int main() {
    char s[100]; // Assuming input string length won't exceed 100
    scanf("%s", s);

    // Compile the regular expression
    regex_t regex;
    int reti = regcomp(&regex, "^1(0+)?$", REG_EXTENDED);

    if (reti) {
        fprintf(stderr, "Could not compile regex\n");
        return 1;
    }

    // Execute the regular expression match
    reti = regexec(&regex, s, 0, NULL, 0);
    
    // Print the result of the match
    if (!reti) {
        printf("true\n");
    } else if (reti == REG_NOMATCH) {
        printf("false\n");
    } else {
        char msgbuf[100];
        regerror(reti, &regex, msgbuf, sizeof(msgbuf));
        fprintf(stderr, "Regex match failed: %s\n", msgbuf);
        return 1;
    }

    // Free the compiled regular expression
    regfree(&regex);
    
    return 0;
}
