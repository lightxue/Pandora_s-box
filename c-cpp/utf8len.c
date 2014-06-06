int utf8len(const char * s, int len)
{
    int cnt = 0;
    int i = 0;
    while (i < len) {
        if ((s[i] & 0xc0) != 0x80) {
            cnt++;
        }
        i++;
    }
    return cnt;
}
