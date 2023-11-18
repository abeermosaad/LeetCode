int lengthOfLastWord(char* s) {
    int len = strlen(s), flag = 0, cnt = 0;
    for (int i = len - 1 ; i >= 0; i--)
    {
        if (s[i] == ' ' && flag == 1)
            break;
        if (s[i] != ' ' && flag == 0)
            flag = 1;
        if (flag == 1)
            cnt++;
    }
    return cnt;
}
