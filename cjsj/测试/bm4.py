def js(open,high,low,close):   
    d=0
    x=0
    if(open>=close):
        d=open
        x=close
    if(open<close):
        d=close
        x=open
    
    h=high-d
    l=x-low
       
    return h,l


#openzl=[[-10.6,-9.94],[-9.94,-7],[-7,-3],[-3,-1],[-1,1],[1,3],[3,7],[7,9.94],[9.94,10.6]]
#closezl=[[-10.6,-9.94],[-9.94,-7],[-7,-4],[-4,-2],[-2,-1],[-1,0],[0,1],[1,2],[2,4],[4,7],[7,9.94],[9.94,10.6]]
#normzl=[[0,1.5],[1.5,3.5],[3.5,20.5]]


def bm(open,high,low,close):
    num=0
    if(open>=-10.6 and open<=-9.94):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=1
            if(h>=1.5 and h<3.5):
                num=2
            if(h>=3.5 and h<=20.5):
                num=3
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=4
            if(h>=1.5 and h<3.5):
                num=5
            if(h>=3.5 and h<=20.5):
                num=6
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=7
            if(h>=1.5 and h<3.5):
                num=8
            if(h>=3.5 and h<=20.5):
                num=9
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=10
            if(h>=1.5 and h<3.5):
                num=11
            if(h>=3.5 and h<=20.5):
                num=12
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=13
            if(h>=1.5 and h<3.5):
                num=14
            if(h>=3.5 and h<=20.5):
                num=15
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=16
            if(h>=1.5 and h<3.5):
                num=17
            if(h>=3.5 and h<=20.5):
                num=18
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=19
            if(h>=1.5 and h<3.5):
                num=20
            if(h>=3.5 and h<=20.5):
                num=21
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=22
            if(h>=1.5 and h<3.5):
                num=23
            if(h>=3.5 and h<=20.5):
                num=24
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=25
            if(h>=1.5 and h<3.5):
                num=26
            if(h>=3.5 and h<=20.5):
                num=27
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=28
            if(h>=1.5 and h<3.5):
                num=29
            if(h>=3.5 and h<=20.5):
                num=30
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=31
            if(h>=1.5 and h<3.5):
                num=32
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            num=33





    if(open>-9.94 and open<-7):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=34
            if(h>=1.5 and h<3.5):
                num=35
            if(h>=3.5 and h<=20.5):
                num=36
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=37
                if(l>=1.5 and l<3.5):
                    num=38
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=39
                if(l>=1.5 and l<3.5):
                    num=40
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=41
                if(l>=1.5 and l<3.5):
                    num=42
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=43
                if(l>=1.5 and l<3.5):
                    num=44
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=45
                if(l>=1.5 and l<3.5):
                    num=46
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=47
                if(l>=1.5 and l<3.5):
                    num=48
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=49
                if(l>=1.5 and l<3.5):
                    num=50
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=51
                if(l>=1.5 and l<3.5):
                    num=52
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=53
                if(l>=1.5 and l<3.5):
                    num=54
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=55
                if(l>=1.5 and l<3.5):
                    num=56
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=57
                if(l>=1.5 and l<3.5):
                    num=58
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=59
                if(l>=1.5 and l<3.5):
                    num=60
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=61
                if(l>=1.5 and l<3.5):
                    num=62
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=63
                if(l>=1.5 and l<3.5):
                    num=64
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=65
                if(l>=1.5 and l<3.5):
                    num=66
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=67
                if(l>=1.5 and l<3.5):
                    num=68
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=69
                if(l>=1.5 and l<3.5):
                    num=70
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=71
                if(l>=1.5 and l<3.5):
                    num=72
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=73
                if(l>=1.5 and l<3.5):
                    num=74
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=75
                if(l>=1.5 and l<3.5):
                    num=76
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=77
                if(l>=1.5 and l<3.5):
                    num=78
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=79
                if(l>=1.5 and l<3.5):
                    num=80
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=81
                if(l>=1.5 and l<3.5):
                    num=82
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=83
                if(l>=1.5 and l<3.5):
                    num=84
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=85
                if(l>=1.5 and l<3.5):
                    num=86
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=87
                if(l>=1.5 and l<3.5):
                    num=88
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=89
                if(l>=1.5 and l<3.5):
                    num=90
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=91
                if(l>=1.5 and l<3.5):
                    num=92
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=93
                if(l>=1.5 and l<3.5):
                    num=94
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=95
            if(l>=1.5 and l<3.5):
                num=96



    if(open>=-7 and open<-3):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=97
            if(h>=1.5 and h<3.5):
                num=98
            if(h>=3.5 and h<=20.5):
                num=99
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=100
                if(l>=1.5 and l<3.5):
                    num=101
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=102
                if(l>=1.5 and l<3.5):
                    num=103
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=104
                if(l>=1.5 and l<3.5):
                    num=105
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=106
                if(l>=1.5 and l<3.5):
                    num=107
                if(l>=3.5 and l<20.5):
                    num=108
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=109
                if(l>=1.5 and l<3.5):
                    num=110
                if(l>=3.5 and l<20.5):
                    num=111
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=112
                if(l>=1.5 and l<3.5):
                    num=113
                if(l>=3.5 and l<20.5):
                    num=114
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=115
                if(l>=1.5 and l<3.5):
                    num=116
                if(l>=3.5 and l<=20.5):
                    num=117
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=118
                if(l>=1.5 and l<3.5):
                    num=119
                if(l>=3.5 and l<=20.5):
                    num=120
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=121
                if(l>=1.5 and l<3.5):
                    num=122
                if(l>=3.5 and l<=20.5):
                    num=123
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=124
                if(l>=1.5 and l<3.5):
                    num=125
                if(l>=3.5 and l<=20.5):
                    num=126
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=127
                if(l>=1.5 and l<3.5):
                    num=128
                if(l>=3.5 and l<=20.5):
                    num=129
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=130
                if(l>=1.5 and l<3.5):
                    num=131
                if(l>=3.5 and l<=20.5):
                    num=132
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=133
                if(l>=1.5 and l<3.5):
                    num=134
                if(l>=3.5 and l<=20.5):
                    num=135
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=136
                if(l>=1.5 and l<3.5):
                    num=137
                if(l>=3.5 and l<=20.5):
                    num=138
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=139
                if(l>=1.5 and l<3.5):
                    num=140
                if(l>=3.5 and l<=20.5):
                    num=141
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=142
                if(l>=1.5 and l<3.5):
                    num=143
                if(l>=3.5 and l<=20.5):
                    num=144
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=145
                if(l>=1.5 and l<3.5):
                    num=146
                if(l>=3.5 and l<=20.5):
                    num=147
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=148
                if(l>=1.5 and l<3.5):
                    num=149
                if(l>=3.5 and l<=20.5):
                    num=150
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=151
                if(l>=1.5 and l<3.5):
                    num=152
                if(l>=3.5 and l<=20.5):
                    num=153
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=154
                if(l>=1.5 and l<3.5):
                    num=155
                if(l>=3.5 and l<=20.5):
                    num=156
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=157
                if(l>=1.5 and l<3.5):
                    num=158
                if(l>=3.5 and l<=20.5):
                    num=159
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=160
                if(l>=1.5 and l<3.5):
                    num=161
                if(l>=3.5 and l<=20.5):
                    num=162
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=163
                if(l>=1.5 and l<3.5):
                    num=164
                if(l>=3.5 and l<=20.5):
                    num=165
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=166
                if(l>=1.5 and l<3.5):
                    num=167
                if(l>=3.5 and l<=20.5):
                    num=168
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=169
                if(l>=1.5 and l<3.5):
                    num=170
                if(l>=3.5 and l<=20.5):
                    num=171
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=172
                if(l>=1.5 and l<3.5):
                    num=173
                if(l>=3.5 and l<=20.5):
                    num=174
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=175
                if(l>=1.5 and l<3.5):
                    num=176
                if(l>=3.5 and l<=20.5):
                    num=177
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=178
                if(l>=1.5 and l<3.5):
                    num=179
                if(l>=3.5 and l<=20.5):
                    num=180
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=181
                if(l>=1.5 and l<3.5):
                    num=182
                if(l>=3.5 and l<=20.5):
                    num=183
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=184
            if(l>=1.5 and l<3.5):
                num=185
            if(l>=3.5 and l<=20.5):
                num=186




    if(open>=-3 and open<-1):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=187
            if(h>=1.5 and h<3.5):
                num=188
            if(h>=3.5 and h<=20.5):
                num=189
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=190
                if(l>=1.5 and l<3.5):
                    num=191
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=192
                if(l>=1.5 and l<3.5):
                    num=193
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=194
                if(l>=1.5 and l<3.5):
                    num=195
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=196
                if(l>=1.5 and l<3.5):
                    num=197
                if(l>=3.5 and l<20.5):
                    num=198
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=199
                if(l>=1.5 and l<3.5):
                    num=200
                if(l>=3.5 and l<20.5):
                    num=201
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=202
                if(l>=1.5 and l<3.5):
                    num=203
                if(l>=3.5 and l<20.5):
                    num=204
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=205
                if(l>=1.5 and l<3.5):
                    num=206
                if(l>=3.5 and l<=20.5):
                    num=207
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=208
                if(l>=1.5 and l<3.5):
                    num=209
                if(l>=3.5 and l<=20.5):
                    num=210
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=211
                if(l>=1.5 and l<3.5):
                    num=212
                if(l>=3.5 and l<=20.5):
                    num=213
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=214
                if(l>=1.5 and l<3.5):
                    num=215
                if(l>=3.5 and l<=20.5):
                    num=216
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=217
                if(l>=1.5 and l<3.5):
                    num=218
                if(l>=3.5 and l<=20.5):
                    num=219
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=220
                if(l>=1.5 and l<3.5):
                    num=221
                if(l>=3.5 and l<=20.5):
                    num=222
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=223
                if(l>=1.5 and l<3.5):
                    num=224
                if(l>=3.5 and l<=20.5):
                    num=225
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=226
                if(l>=1.5 and l<3.5):
                    num=227
                if(l>=3.5 and l<=20.5):
                    num=228
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=229
                if(l>=1.5 and l<3.5):
                    num=230
                if(l>=3.5 and l<=20.5):
                    num=231
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=232
                if(l>=1.5 and l<3.5):
                    num=233
                if(l>=3.5 and l<=20.5):
                    num=234
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=235
                if(l>=1.5 and l<3.5):
                    num=236
                if(l>=3.5 and l<=20.5):
                    num=237
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=238
                if(l>=1.5 and l<3.5):
                    num=239
                if(l>=3.5 and l<=20.5):
                    num=240
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=241
                if(l>=1.5 and l<3.5):
                    num=242
                if(l>=3.5 and l<=20.5):
                    num=243
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=244
                if(l>=1.5 and l<3.5):
                    num=245
                if(l>=3.5 and l<=20.5):
                    num=246
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=247
                if(l>=1.5 and l<3.5):
                    num=248
                if(l>=3.5 and l<=20.5):
                    num=249
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=250
                if(l>=1.5 and l<3.5):
                    num=251
                if(l>=3.5 and l<=20.5):
                    num=252
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=253
                if(l>=1.5 and l<3.5):
                    num=254
                if(l>=3.5 and l<=20.5):
                    num=255
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=256
                if(l>=1.5 and l<3.5):
                    num=257
                if(l>=3.5 and l<=20.5):
                    num=258
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=259
                if(l>=1.5 and l<3.5):
                    num=260
                if(l>=3.5 and l<=20.5):
                    num=261
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=262
                if(l>=1.5 and l<3.5):
                    num=263
                if(l>=3.5 and l<=20.5):
                    num=264
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=265
                if(l>=1.5 and l<3.5):
                    num=266
                if(l>=3.5 and l<=20.5):
                    num=267
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=268
                if(l>=1.5 and l<3.5):
                    num=269
                if(l>=3.5 and l<=20.5):
                    num=270
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=271
                if(l>=1.5 and l<3.5):
                    num=272
                if(l>=3.5 and l<=20.5):
                    num=273
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=274
            if(l>=1.5 and l<3.5):
                num=275
            if(l>=3.5 and l<=20.5):
                num=276



    if(open>=-1 and open<1):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=277
            if(h>=1.5 and h<3.5):
                num=278
            if(h>=3.5 and h<=20.5):
                num=279
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=280
                if(l>=1.5 and l<3.5):
                    num=281
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=282
                if(l>=1.5 and l<3.5):
                    num=283
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=284
                if(l>=1.5 and l<3.5):
                    num=285
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=286
                if(l>=1.5 and l<3.5):
                    num=287
                if(l>=3.5 and l<20.5):
                    num=288
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=289
                if(l>=1.5 and l<3.5):
                    num=290
                if(l>=3.5 and l<20.5):
                    num=291
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=292
                if(l>=1.5 and l<3.5):
                    num=293
                if(l>=3.5 and l<20.5):
                    num=294
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=295
                if(l>=1.5 and l<3.5):
                    num=296
                if(l>=3.5 and l<=20.5):
                    num=297
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=298
                if(l>=1.5 and l<3.5):
                    num=299
                if(l>=3.5 and l<=20.5):
                    num=300
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=301
                if(l>=1.5 and l<3.5):
                    num=302
                if(l>=3.5 and l<=20.5):
                    num=303
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=304
                if(l>=1.5 and l<3.5):
                    num=305
                if(l>=3.5 and l<=20.5):
                    num=306
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=307
                if(l>=1.5 and l<3.5):
                    num=308
                if(l>=3.5 and l<=20.5):
                    num=309
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=310
                if(l>=1.5 and l<3.5):
                    num=311
                if(l>=3.5 and l<=20.5):
                    num=312
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=313
                if(l>=1.5 and l<3.5):
                    num=314
                if(l>=3.5 and l<=20.5):
                    num=315
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=316
                if(l>=1.5 and l<3.5):
                    num=317
                if(l>=3.5 and l<=20.5):
                    num=318
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=319
                if(l>=1.5 and l<3.5):
                    num=320
                if(l>=3.5 and l<=20.5):
                    num=321
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=322
                if(l>=1.5 and l<3.5):
                    num=323
                if(l>=3.5 and l<=20.5):
                    num=324
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=325
                if(l>=1.5 and l<3.5):
                    num=326
                if(l>=3.5 and l<=20.5):
                    num=327
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=328
                if(l>=1.5 and l<3.5):
                    num=329
                if(l>=3.5 and l<=20.5):
                    num=330
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=331
                if(l>=1.5 and l<3.5):
                    num=332
                if(l>=3.5 and l<=20.5):
                    num=333
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=334
                if(l>=1.5 and l<3.5):
                    num=335
                if(l>=3.5 and l<=20.5):
                    num=336
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=337
                if(l>=1.5 and l<3.5):
                    num=338
                if(l>=3.5 and l<=20.5):
                    num=339
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=340
                if(l>=1.5 and l<3.5):
                    num=341
                if(l>=3.5 and l<=20.5):
                    num=342
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=343
                if(l>=1.5 and l<3.5):
                    num=344
                if(l>=3.5 and l<=20.5):
                    num=345
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=346
                if(l>=1.5 and l<3.5):
                    num=347
                if(l>=3.5 and l<=20.5):
                    num=348
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=349
                if(l>=1.5 and l<3.5):
                    num=350
                if(l>=3.5 and l<=20.5):
                    num=351
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=352
                if(l>=1.5 and l<3.5):
                    num=353
                if(l>=3.5 and l<=20.5):
                    num=354
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=355
                if(l>=1.5 and l<3.5):
                    num=356
                if(l>=3.5 and l<=20.5):
                    num=357
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=358
                if(l>=1.5 and l<3.5):
                    num=359
                if(l>=3.5 and l<=20.5):
                    num=360
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=361
                if(l>=1.5 and l<3.5):
                    num=362
                if(l>=3.5 and l<=20.5):
                    num=363
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=364
            if(l>=1.5 and l<3.5):
                num=365
            if(l>=3.5 and l<=20.5):
                num=366


    if(open>=1 and open<3):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=367
            if(h>=1.5 and h<3.5):
                num=368
            if(h>=3.5 and h<=20.5):
                num=369
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=370
                if(l>=1.5 and l<3.5):
                    num=371
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=372
                if(l>=1.5 and l<3.5):
                    num=373
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=374
                if(l>=1.5 and l<3.5):
                    num=375
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=376
                if(l>=1.5 and l<3.5):
                    num=377
                if(l>=3.5 and l<20.5):
                    num=378
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=379
                if(l>=1.5 and l<3.5):
                    num=380
                if(l>=3.5 and l<20.5):
                    num=381
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=382
                if(l>=1.5 and l<3.5):
                    num=383
                if(l>=3.5 and l<20.5):
                    num=384
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=385
                if(l>=1.5 and l<3.5):
                    num=386
                if(l>=3.5 and l<=20.5):
                    num=387
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=388
                if(l>=1.5 and l<3.5):
                    num=389
                if(l>=3.5 and l<=20.5):
                    num=390
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=391
                if(l>=1.5 and l<3.5):
                    num=392
                if(l>=3.5 and l<=20.5):
                    num=393
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=394
                if(l>=1.5 and l<3.5):
                    num=395
                if(l>=3.5 and l<=20.5):
                    num=396
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=397
                if(l>=1.5 and l<3.5):
                    num=398
                if(l>=3.5 and l<=20.5):
                    num=399
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=400
                if(l>=1.5 and l<3.5):
                    num=401
                if(l>=3.5 and l<=20.5):
                    num=402
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=403
                if(l>=1.5 and l<3.5):
                    num=404
                if(l>=3.5 and l<=20.5):
                    num=405
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=406
                if(l>=1.5 and l<3.5):
                    num=407
                if(l>=3.5 and l<=20.5):
                    num=408
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=409
                if(l>=1.5 and l<3.5):
                    num=410
                if(l>=3.5 and l<=20.5):
                    num=411
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=412
                if(l>=1.5 and l<3.5):
                    num=413
                if(l>=3.5 and l<=20.5):
                    num=414
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=415
                if(l>=1.5 and l<3.5):
                    num=416
                if(l>=3.5 and l<=20.5):
                    num=417
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=418
                if(l>=1.5 and l<3.5):
                    num=419
                if(l>=3.5 and l<=20.5):
                    num=420
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=421
                if(l>=1.5 and l<3.5):
                    num=422
                if(l>=3.5 and l<=20.5):
                    num=423
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=424
                if(l>=1.5 and l<3.5):
                    num=425
                if(l>=3.5 and l<=20.5):
                    num=426
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=427
                if(l>=1.5 and l<3.5):
                    num=428
                if(l>=3.5 and l<=20.5):
                    num=429
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=430
                if(l>=1.5 and l<3.5):
                    num=431
                if(l>=3.5 and l<=20.5):
                    num=432
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=433
                if(l>=1.5 and l<3.5):
                    num=434
                if(l>=3.5 and l<=20.5):
                    num=435
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=436
                if(l>=1.5 and l<3.5):
                    num=437
                if(l>=3.5 and l<=20.5):
                    num=438
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=439
                if(l>=1.5 and l<3.5):
                    num=440
                if(l>=3.5 and l<=20.5):
                    num=441
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=442
                if(l>=1.5 and l<3.5):
                    num=443
                if(l>=3.5 and l<=20.5):
                    num=444
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=445
                if(l>=1.5 and l<3.5):
                    num=446
                if(l>=3.5 and l<=20.5):
                    num=447
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=448
                if(l>=1.5 and l<3.5):
                    num=449
                if(l>=3.5 and l<=20.5):
                    num=450
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=451
                if(l>=1.5 and l<3.5):
                    num=452
                if(l>=3.5 and l<=20.5):
                    num=453
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=454
            if(l>=1.5 and l<3.5):
                num=455
            if(l>=3.5 and l<=20.5):
                num=456




    if(open>=3 and open<7):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=457
            if(h>=1.5 and h<3.5):
                num=458
            if(h>=3.5 and h<=20.5):
                num=459
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=460
                if(l>=1.5 and l<3.5):
                    num=461
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=462
                if(l>=1.5 and l<3.5):
                    num=463
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=464
                if(l>=1.5 and l<3.5):
                    num=465
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=466
                if(l>=1.5 and l<3.5):
                    num=467
                if(l>=3.5 and l<20.5):
                    num=468
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=469
                if(l>=1.5 and l<3.5):
                    num=470
                if(l>=3.5 and l<20.5):
                    num=471
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=472
                if(l>=1.5 and l<3.5):
                    num=473
                if(l>=3.5 and l<20.5):
                    num=474
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=475
                if(l>=1.5 and l<3.5):
                    num=476
                if(l>=3.5 and l<=20.5):
                    num=477
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=478
                if(l>=1.5 and l<3.5):
                    num=479
                if(l>=3.5 and l<=20.5):
                    num=480
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=481
                if(l>=1.5 and l<3.5):
                    num=482
                if(l>=3.5 and l<=20.5):
                    num=483
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=484
                if(l>=1.5 and l<3.5):
                    num=485
                if(l>=3.5 and l<=20.5):
                    num=486
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=487
                if(l>=1.5 and l<3.5):
                    num=488
                if(l>=3.5 and l<=20.5):
                    num=489
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=490
                if(l>=1.5 and l<3.5):
                    num=491
                if(l>=3.5 and l<=20.5):
                    num=492
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=493
                if(l>=1.5 and l<3.5):
                    num=494
                if(l>=3.5 and l<=20.5):
                    num=495
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=496
                if(l>=1.5 and l<3.5):
                    num=497
                if(l>=3.5 and l<=20.5):
                    num=498
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=499
                if(l>=1.5 and l<3.5):
                    num=500
                if(l>=3.5 and l<=20.5):
                    num=501
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=502
                if(l>=1.5 and l<3.5):
                    num=503
                if(l>=3.5 and l<=20.5):
                    num=504
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=505
                if(l>=1.5 and l<3.5):
                    num=506
                if(l>=3.5 and l<=20.5):
                    num=507
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=508
                if(l>=1.5 and l<3.5):
                    num=509
                if(l>=3.5 and l<=20.5):
                    num=510
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=511
                if(l>=1.5 and l<3.5):
                    num=512
                if(l>=3.5 and l<=20.5):
                    num=513
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=514
                if(l>=1.5 and l<3.5):
                    num=515
                if(l>=3.5 and l<=20.5):
                    num=516
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=517
                if(l>=1.5 and l<3.5):
                    num=518
                if(l>=3.5 and l<=20.5):
                    num=519
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=520
                if(l>=1.5 and l<3.5):
                    num=521
                if(l>=3.5 and l<=20.5):
                    num=522
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=523
                if(l>=1.5 and l<3.5):
                    num=524
                if(l>=3.5 and l<=20.5):
                    num=525
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=526
                if(l>=1.5 and l<3.5):
                    num=527
                if(l>=3.5 and l<=20.5):
                    num=528
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=529
                if(l>=1.5 and l<3.5):
                    num=530
                if(l>=3.5 and l<=20.5):
                    num=531
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=532
                if(l>=1.5 and l<3.5):
                    num=533
                if(l>=3.5 and l<=20.5):
                    num=534
            if(h>=3.5 and h<=20.5):
                if(l>=0 and l<1.5):
                    num=535
                if(l>=1.5 and l<3.5):
                    num=536
                if(l>=3.5 and l<=20.5):
                    num=537
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=538
                if(l>=1.5 and l<3.5):
                    num=539
                if(l>=3.5 and l<=20.5):
                    num=540
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=541
                if(l>=1.5 and l<3.5):
                    num=542
                if(l>=3.5 and l<=20.5):
                    num=543
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=544
            if(l>=1.5 and l<3.5):
                num=545
            if(l>=3.5 and l<=20.5):
                num=546



    if(open>=7 and open<9.94):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                num=547
            if(h>=1.5 and h<3.5):
                num=548
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=549
                if(l>=1.5 and l<3.5):
                    num=550
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=551
                if(l>=1.5 and l<3.5):
                    num=552
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=553
                if(l>=1.5 and l<3.5):
                    num=554
                if(l>=3.5 and l<20.5):
                    num=555
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=556
                if(l>=1.5 and l<3.5):
                    num=557
                if(l>=3.5 and l<20.5):
                    num=558
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=559
                if(l>=1.5 and l<3.5):
                    num=560
                if(l>=3.5 and l<=20.5):
                    num=561
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=562
                if(l>=1.5 and l<3.5):
                    num=563
                if(l>=3.5 and l<=20.5):
                    num=564
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=565
                if(l>=1.5 and l<3.5):
                    num=566
                if(l>=3.5 and l<=20.5):
                    num=567
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=568
                if(l>=1.5 and l<3.5):
                    num=569
                if(l>=3.5 and l<=20.5):
                    num=570
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=571
                if(l>=1.5 and l<3.5):
                    num=572
                if(l>=3.5 and l<=20.5):
                    num=573
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=574
                if(l>=1.5 and l<3.5):
                    num=575
                if(l>=3.5 and l<=20.5):
                    num=576
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=577
                if(l>=1.5 and l<3.5):
                    num=578
                if(l>=3.5 and l<=20.5):
                    num=579
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=580
                if(l>=1.5 and l<3.5):
                    num=581
                if(l>=3.5 and l<=20.5):
                    num=582
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=583
                if(l>=1.5 and l<3.5):
                    num=584
                if(l>=3.5 and l<=20.5):
                    num=585
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=586
                if(l>=1.5 and l<3.5):
                    num=587
                if(l>=3.5 and l<=20.5):
                    num=588
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=589
                if(l>=1.5 and l<3.5):
                    num=590
                if(l>=3.5 and l<=20.5):
                    num=591
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=592
                if(l>=1.5 and l<3.5):
                    num=593
                if(l>=3.5 and l<=20.5):
                    num=594
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=595
                if(l>=1.5 and l<3.5):
                    num=596
                if(l>=3.5 and l<=20.5):
                    num=597
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=598
                if(l>=1.5 and l<3.5):
                    num=599
                if(l>=3.5 and l<=20.5):
                    num=600
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(h>=0 and h<1.5):
                if(l>=0 and l<1.5):
                    num=601
                if(l>=1.5 and l<3.5):
                    num=602
                if(l>=3.5 and l<=20.5):
                    num=603
            if(h>=1.5 and h<3.5):
                if(l>=0 and l<1.5):
                    num=604
                if(l>=1.5 and l<3.5):
                    num=605
                if(l>=3.5 and l<=20.5):
                    num=606
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=607
            if(l>=1.5 and l<3.5):
                num=608
            if(l>=3.5 and l<=20.5):
                num=609



    if(open>=9.94 and open<=10.6):
        if(close>=-10.6 and close<=-9.94):
            h,l=js(open,high,low,close)
            num=610
        if(close>-9.94 and close<-7):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=611
            if(l>=1.5 and l<3.5):
                num=612
        if(close>=-7 and close<-4):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=613
            if(l>=1.5 and l<3.5):
                num=614
            if(l>=3.5 and l<20.5):
                num=615
        if(close>=-4 and close<-2):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=616
            if(l>=1.5 and l<3.5):
                num=617
            if(l>=3.5 and l<=20.5):
                num=618
        if(close>=-2 and close<-1):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=619
            if(l>=1.5 and l<3.5):
                num=620
            if(l>=3.5 and l<=20.5):
                num=621
        if(close>=-1 and close<0):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=622
            if(l>=1.5 and l<3.5):
                num=623
            if(l>=3.5 and l<=20.5):
                num=624
        if(close>=0 and close<1):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=625
            if(l>=1.5 and l<3.5):
                num=626
            if(l>=3.5 and l<=20.5):
                num=627
        if(close>=1 and close<2):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=628
            if(l>=1.5 and l<3.5):
                num=629
            if(l>=3.5 and l<=20.5):
                num=630
        if(close>=2 and close<4):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=631
            if(l>=1.5 and l<3.5):
                num=632
            if(l>=3.5 and l<=20.5):
                num=633
        if(close>=4 and close<7):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=634
            if(l>=1.5 and l<3.5):
                num=635
            if(l>=3.5 and l<=20.5):
                num=636
        if(close>=7 and close<9.94):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=637
            if(l>=1.5 and l<3.5):
                num=638
            if(l>=3.5 and l<=20.5):
                num=639
        if(close>=9.94 and close<=10.6):
            h,l=js(open,high,low,close)
            if(l>=0 and l<1.5):
                num=640
            if(l>=1.5 and l<3.5):
                num=641
            if(l>=3.5 and l<=20.5):
                num=642
                
    return num
