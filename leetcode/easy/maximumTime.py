class Solution:
    def maximumTime(self, time: str) -> str:
        pos0 = {'2':'3','1':'9', '0':'9'}
        pos3 = '5'
        pos4 = '9'
        new_time = []
        for i, char in enumerate(time):
            if char == '?':
                if i == 0:
                    if (time[1] == '0' or time[1] == '1' or time[1] == '2' or time[1] == '3' or time[1] == '?') :
                        new_time.append('2')
                    else:
                        new_time.append('1')
                elif i == 1:
                    new_time.append(pos0[new_time[0]])
                elif i == 3:
                    new_time.append(pos3)
                else:
                    new_time.append(pos4)
            else:
                new_time.append(char)
                    
        return ''.join(new_time)
