function isAnagram(s: string, t: string): boolean {
    if (s.length != t.length) {
        return false;
    }
    let str1 = s.split('')
    let str2 = t.split('')
    const sortf = (a,b) => {
        if (a < b) {
            return -1;
        }
        if (a > b) {
            return 1;
        }
        return 0;
    }
    str1.sort(sortf);
    str2.sort(sortf);
    return str1.every((val, index) => val === str2[index]);
};