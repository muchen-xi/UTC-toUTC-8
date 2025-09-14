rtc = RTC()
        now_time = list(rtc.datetime())
        print(now_time)
        now_time[4] = now_time[4] + 8
        if now_time[4] >= 24:
            now_time[4] = now_time[4] - 24
            now_time[2] = now_time[2] + 1
            for i in [1, 3, 5, 7, 8, 12]:
                if now_time[1] == i and now_time[2] > 31:
                    now_time[2] = 1
                    now_time[1] = now_time[1] + 1
            for i in [4, 6, 9, 11]:
                if now_time[1] == i and now_time[2] > 30:
                    now_time[2] = 1
                    now_time[1] = now_time[1] + 1
            if now_time[1] == 2:
                ac = now_time[0]
                if ac % 4 == 0 and now_time[2] > 29:
                    now_time[2] = 1
                    now_time[1] = now_time[1] + 1
                elif ac % 4 > 0 and now_time[2] > 28:
                    now_time[2] = 1
                    now_time[1] = now_time[1] + 1
            if now_time[1] > 13:
                now_time[1] = 1
                now_time += 1