'''
https://leetcode-cn.com/contest/cnunionpay-2022spring/problems/kDPV0f/

题目没有说明 priceLimit 越大，discount 越大。
下面用了binary search, 但是只是二分了price。 找到索引后，还是要遍历下剩余的discount。

62 / 62 个通过测试用例
状态：通过
执行用时: 248 ms
内存消耗: 15.7 MB
'''

class DiscountSystem:

    def __init__(self):
        self.pl_actId = []
        self.actId2discount = defaultdict(int) 
        self.actId2number = defaultdict(int) 
        self.actId2userLimit = defaultdict(int) 
        # for user
        self.user_cnt = defaultdict(Counter)

    def addActivity(self, actId: int, priceLimit: int, discount: int, number: int, userLimit: int) -> None:
        bisect.insort(self.pl_actId, (priceLimit, actId))
        self.actId2discount[actId] = discount 
        self.actId2number[actId] = number
        self.actId2userLimit[actId] = userLimit

    def removeActivity(self, actId: int) -> None:
        self.actId2discount.pop(actId, -1)
        self.actId2number.pop(actId, -1)
        self.actId2userLimit.pop(actId, -1)

    def consume(self, userId: int, cost: int) -> int:
        # find actId
        actId = None 
        n = len(self.pl_actId)
        idx = bisect_right(self.pl_actId, (cost, 1003)) - 1
        while idx >= 0:
            pl, act = self.pl_actId[idx]
            if act not in self.actId2discount:
                idx -= 1
                continue            
            if self.user_cnt[userId][act] < self.actId2userLimit[act]:
                if actId is None:   #  if not actId: # wrong, actId 可能为 0
                    actId = act 
                elif self.actId2discount[actId] < self.actId2discount[act] or (self.actId2discount[actId] == self.actId2discount[act] and act < actId):
                    actId = act 
            idx -= 1
            
        if actId is None:   #  if not actId: # wrong, actId 可能为 0
            return cost 
        # discount
        self.user_cnt[userId][actId] += 1
        ans = cost - self.actId2discount[actId]
        self.actId2number[actId] -= 1
        if 0 == self.actId2number[actId]:
            self.removeActivity(actId)
        return ans 

# Your DiscountSystem object will be instantiated and called as such:
# obj = DiscountSystem()
# obj.addActivity(actId,priceLimit,discount,number,userLimit)
# obj.removeActivity(actId)
# param_3 = obj.consume(userId,cost)




'''
["DiscountSystem","addActivity","consume","removeActivity","consume"]
[[],[1,15,5,7,2],[101,16],[1],[102,19]]
["DiscountSystem","addActivity","addActivity","consume","removeActivity","consume","consume","consume","consume"]
[[],[1,10,6,3,2],[2,15,8,8,2],[101,13],[2],[101,17],[101,11],[102,16],[102,21]]


## if actId is None:   #  if not actId: # wrong, actId 可能为 0    # 51行
输入：["DiscountSystem","addActivity","consume","consume","consume","consume","consume","consume","consume"]
[[],[0,48,21,8,7],[8,59],[8,33],[8,55],[8,21],[8,45],[6,81],[9,50]]
输出：[null,null,59,33,55,21,45,81,50]
预期：[null,null,38,33,34,21,45,60,29]

## if actId is None:   #  if not actId: # wrong, actId 可能为 0     # 45行
输入：["DiscountSystem","consume","consume","addActivity","consume","addActivity","consume","consume","addActivity","addActivity","addActivity","consume","consume","addActivity","removeActivity","consume","consume","consume","addActivity","consume","addActivity","consume","consume","removeActivity","removeActivity","removeActivity","addActivity","consume","consume","consume","consume","removeActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","removeActivity","removeActivity","addActivity","removeActivity","consume","removeActivity","addActivity","addActivity","removeActivity","consume","addActivity","removeActivity","consume","removeActivity","consume","consume","removeActivity","consume","consume","consume","addActivity","consume","addActivity","consume","consume","consume","consume","addActivity","consume","removeActivity","consume","consume","addActivity","removeActivity","consume","removeActivity","addActivity","consume","addActivity","consume","addActivity","addActivity","addActivity","addActivity","removeActivity","consume","removeActivity","addActivity","addActivity","addActivity"]
[[],[16,412],[12,950],[14,507,198,17,6],[7,982],[81,414,121,27,8],[16,602],[17,328],[79,459,192,21,10],[60,489,146,42,5],[4,431,166,24,1],[12,570],[17,953],[10,485,141,19,4],[79],[12,331],[75,749],[65,418],[68,479,125,31,9],[7,643],[27,388,156,42,9],[12,806],[65,864],[81],[68],[60],[0,484,241,22,4],[7,490],[7,727],[36,673],[81,768],[14],[12,436],[12,509],[65,715],[7,804],[7,882],[75,979],[17,681],[17,548],[57,240],[27],[10],[88,546,110,43,8],[88],[65,422],[0],[50,576,197,37,9],[86,485,124,39,4],[50],[12,261],[30,397,134,43,5],[30],[7,423],[86],[36,341],[17,292],[4],[17,997],[75,848],[75,209],[48,535,214,30,9],[81,482],[70,560,141,22,10],[16,279],[81,479],[57,871],[75,968],[1,554,162,43,10],[36,674],[1],[7,916],[57,375],[74,573,157,28,1],[48],[81,570],[74],[39,481,184,36,4],[17,318],[61,577,172,23,3],[36,969],[12,538,211,43,8],[8,443,128,43,5],[46,478,226,22,6],[16,511,203,24,8],[70],[15,214],[12],[43,475,173,18,9],[49,565,235,32,5],[25,561,227,18,10]]
输出：[null,412,950,null,784,null,404,328,null,null,null,372,755,null,null,331,551,297,null,445,null,608,666,null,null,null,null,324,571,507,602,null,270,353,549,648,726,813,515,392,240,null,null,null,null,422,null,null,null,null,261,null,null,423,null,341,292,null,997,848,209,null,482,null,279,479,657,754,null,460,null,702,375,null,null,429,null,null,318,null,785,null,null,null,null,null,214,null,null,null,null]
预期：[null,412,950,null,784,null,404,328,null,null,null,372,755,null,null,331,551,297,null,445,null,608,666,null,null,null,null,249,486,432,527,null,270,268,474,563,641,738,440,307,240,null,null,null,null,422,null,null,null,null,261,null,null,423,null,341,292,null,997,848,209,null,482,null,279,479,657,754,null,460,null,702,375,null,null,429,null,null,318,null,785,null,null,null,null,null,214,null,null,null,null]



KeyError: 756
    self.actId2discount.pop(actId)
Line 22 in removeActivity (Solution.py)
    result = obj.removeActivity(
Line 85 in __helper_select_method__ (Solution.py)
    ret.append(__DriverSolution__().__helper_select_method__(method, params[index], obj))
Line 131 in _driver (Solution.py)
    _driver()
Line 140 in <module> (Solution.py)

# solution
        if actId in self.actId2discount:
            self.actId2discount.pop(actId)
        if actId in self.actId2number:
            self.actId2number.pop(actId)
        if actId in self.actId2userLimit:
            self.actId2userLimit.pop(actId)

https://docs.python.org/3/library/stdtypes.html#typesmapping
pop(key[, default])
If key is in the dictionary, remove it and return its value, else return default. If default is not given and key is not in the dictionary, a KeyError is raised.

# or solution
        self.actId2discount.pop(actId, -1)
        self.actId2number.pop(actId, -1)
        self.actId2userLimit.pop(actId, -1)

["DiscountSystem","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","consume","addActivity","consume","removeActivity","consume","consume","consume","consume","consume","addActivity","consume","consume","addActivity","consume","addActivity","consume","consume","consume","removeActivity","removeActivity","consume","consume","consume","removeActivity","addActivity","consume","addActivity","consume","consume","removeActivity","consume","consume","consume","consume","removeActivity","consume","consume","consume","addActivity","addActivity","consume","removeActivity","consume","consume","consume","addActivity","consume","consume","removeActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","removeActivity","consume","consume","consume","consume","consume","consume","removeActivity","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","removeActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","addActivity","removeActivity","addActivity","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","consume","addActivity","consume","addActivity","consume","removeActivity","consume","consume","addActivity","consume","consume","consume","consume","addActivity","consume","consume","removeActivity","consume","addActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","consume","addActivity","consume","consume","addActivity","consume","consume","consume","addActivity","consume","addActivity","consume","addActivity","consume","consume","consume","consume","consume","removeActivity","consume","consume","consume","addActivity","addActivity","consume","addActivity","addActivity","consume","consume","addActivity","addActivity","addActivity","consume","consume","consume","consume","consume","consume","consume","consume","removeActivity","addActivity","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","addActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","removeActivity","addActivity","consume","consume","consume","consume","consume","consume","consume","addActivity","addActivity","addActivity","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","addActivity","consume","consume","consume","addActivity","addActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","removeActivity","consume","consume","removeActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","addActivity","consume","addActivity","consume","consume","consume","consume","consume","consume","removeActivity","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","consume","consume","consume","removeActivity","addActivity","consume","addActivity","consume","consume","consume","removeActivity","removeActivity","consume","removeActivity","consume","consume","consume","consume","consume","consume","consume","consume","removeActivity","consume","consume","addActivity","removeActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","removeActivity","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","removeActivity","consume","consume","consume","consume","consume","consume","removeActivity","consume","consume","consume","consume","consume","consume","removeActivity","consume","removeActivity","removeActivity","consume","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","consume","consume","consume","removeActivity","consume","consume","consume","consume","removeActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","addActivity","consume","consume","addActivity","consume","addActivity","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","addActivity","consume","removeActivity","consume","consume","removeActivity","consume","addActivity","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","addActivity","consume","consume","consume","addActivity","addActivity","consume","consume","addActivity","consume","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","removeActivity","consume","addActivity","consume","addActivity","consume","consume","consume","consume","consume","addActivity","consume","consume","removeActivity","consume","consume","removeActivity","addActivity","addActivity","consume","consume","consume","addActivity","consume","consume","removeActivity","consume","addActivity","consume","addActivity","consume","consume","addActivity","consume","consume","consume","consume","consume","consume","removeActivity","consume","consume","consume","removeActivity","consume","consume","consume","consume","consume","removeActivity","consume","consume","addActivity","consume","addActivity","consume","consume","addActivity","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","addActivity","consume","addActivity","consume","consume","addActivity","addActivity","consume","consume","consume","consume","consume","consume","addActivity","removeActivity","addActivity","consume","addActivity","consume","consume","consume","addActivity","consume","consume","consume","consume","addActivity","consume","removeActivity","consume","addActivity","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","addActivity","addActivity","consume","addActivity","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","addActivity","addActivity","removeActivity","consume","consume","consume","consume","consume","addActivity","addActivity","consume","removeActivity","consume","addActivity","addActivity","addActivity","addActivity","consume","consume","removeActivity","consume","consume","addActivity","consume","consume","consume","consume","consume","removeActivity","consume","removeActivity","consume","consume","consume","addActivity","addActivity","consume","consume","consume","consume","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","addActivity","addActivity","consume","addActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","removeActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","removeActivity","consume","consume","addActivity","consume","consume","removeActivity","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","consume","removeActivity","removeActivity","consume","consume","consume","consume","consume","consume","addActivity","consume","removeActivity","consume","addActivity","removeActivity","consume","consume","consume","addActivity","consume","consume","consume","consume","consume","addActivity","consume","consume","removeActivity","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","consume","removeActivity","removeActivity","addActivity","consume","removeActivity","consume","consume"]
[[],[664,2380],[664,4380],[379,2468],[664,4673],[379,3945],[594,3253],[594,3013],[172,4822],[529,3811],[483,4849],[270,3472],[865,9668],[483,2940],[669,2884],[601,4872],[83,3928,1864,73,6],[669,3174],[664,3764],[529,5272],[807,3951,1077,56,8],[594,8536],[807],[379,2806],[101,4713],[865,7992],[529,5368],[101,8527],[678,4538,1319,82,8],[379,4124],[669,7608],[835,3663,1093,38,7],[664,4225],[785,5124,2006,83,2],[664,5320],[172,4071],[270,6951],[835],[678],[203,8197],[203,2710],[172,7118],[83],[802,3698,1814,49,5],[594,8020],[179,5415,1888,82,6],[594,2783],[270,3602],[802],[483,4274],[664,7601],[270,7923],[664,7589],[179],[865,4538],[384,8358],[601,4454],[681,5252,1324,50,4],[218,5044,2332,41,3],[83,3125],[681],[594,6621],[172,7791],[483,7215],[648,5041,1779,61,4],[529,3473],[601,6679],[785],[816,5666],[816,6061],[172,4104],[203,9008],[73,7991],[594,5143],[172,9219],[172,8378],[506,3580],[218],[601,9500],[101,6408],[483,7169],[83,3493],[669,4956],[529,9454],[648],[798,9181],[669,4694],[379,8380],[483,5628],[270,7262],[601,6510],[798,6447],[172,6168],[221,5378,1268,54,7],[172,4225],[221],[816,8693],[664,4033],[384,4855],[669,8002],[664,4476],[483,6165],[815,4999],[73,3561],[384,7214],[529,4521,1606,64,7],[483,7091],[659,3700,1713,75,2],[659],[394,4846,1778,48,10],[270,9625],[235,5658],[672,9026],[370,9195],[227,4386,1439,64,8],[384,6354],[498,6509],[669,4957],[597,5061],[601,9974],[865,9274],[900,5216,2268,65,5],[235,2551],[236,4662,1763,79,9],[422,9676],[394],[472,8361],[529,3974],[272,3849,1244,86,5],[83,2319],[664,4853],[72,2217],[422,8944],[639,5013,1545,45,10],[371,5977],[172,6133],[272],[597,5134],[243,4580,2061,82,5],[235,5495],[371,4907],[529,8713],[798,3121],[422,7697],[235,9040],[83,3233],[73,6414],[472,4046],[670,4428,1655,38,6],[203,6168],[865,7974],[840,7160],[677,3684,1505,84,4],[422,8143],[73,9419],[489,4888,1491,77,3],[72,3870],[590,6814],[880,4797],[365,5132,2011,65,10],[533,4086],[84,5335,1317,85,4],[669,8794],[486,4746,2130,73,10],[498,5924],[203,6699],[72,8886],[72,2895],[235,4820],[236],[83,5605],[152,8476],[597,7920],[22,3903,1824,82,3],[96,3861,1862,43,6],[865,5410],[712,4416,1059,44,4],[638,3807,1219,40,5],[865,6036],[480,9066],[695,3991,1834,59,8],[756,5110,2370,46,8],[105,4593,2040,67,10],[371,4074],[72,8521],[409,3883],[152,8245],[798,8681],[370,6165],[816,7493],[36,2731],[96],[72,3864,1931,71,8],[370,3848],[613,8720],[379,7739],[72,4903],[370,3060],[840,7850],[203,3122],[529,9063],[687,4808,1888,83,3],[371,3783],[480,9965],[498,6738],[617,4390],[662,5343,2065,54,8],[480,6616],[613,8698],[371,2196],[22,3537],[172,7755],[880,6946],[172,4307],[798,3579],[317,2549],[36,7902],[845,6555],[754,7089],[669,9449],[371,8064],[132,4723,1306,41,4],[305,9370],[882,4688,1787,78,5],[664,6200],[25,7718],[672,3220],[270,5092],[270,8849],[422,7986],[384,6353],[409,5692],[669,6665],[235,4847],[243],[470,4740,1246,71,7],[493,2094],[533,2786],[152,2304],[808,4136],[686,8470],[601,5954],[409,6677],[608,4253,1274,56,10],[535,5232,2144,64,3],[301,3840,1875,42,8],[25,5554],[22,6353],[126,8990],[261,6527],[888,5328],[529,9743],[720,4593,1752,59,10],[261,8088],[317,4586],[686,6590],[305,2486],[668,3858],[340,4173],[50,2221],[379,4526],[845,4093],[529,3810],[506,6446],[199,2584],[808,9832],[384,2449],[281,4019,1434,69,6],[664,8070],[72,3433],[69,4933,1745,51,9],[199,3480],[317,5744],[808,9772],[437,4170,1034,36,10],[777,5223,2455,48,7],[578,5565],[480,9459],[493,2395],[391,5521],[384,7220],[525,7496],[270,6810],[845,9287],[340,6582],[199,6700],[520,5664],[498,7529],[235,2326],[371,9287],[270,3586],[112,2501],[689,2042],[9,4150,1862,58,3],[687],[840,4038],[498,9178],[281],[50,8474],[54,3138],[379,4710],[480,3746],[146,4153],[816,2130],[689,2598],[296,9148],[597,7412],[108,7742],[242,4695],[447,4567,1477,79,7],[38,5155],[533,3825],[113,4309,1598,57,6],[845,4675],[148,4907,2133,53,9],[633,3933],[664,8914],[633,5388],[400,4882],[506,5215],[498,5058],[9],[177,4747],[664,8778],[422,7820],[270,5242],[472,8676],[840,6240],[83,5019],[146,6352],[172,4424,1653,67,4],[48,7172],[340,4557],[483,8175],[72,3202],[544,5343],[578,9278],[672,4786],[121,4645],[777],[842,4743,1285,83,10],[566,5172],[488,4124,1106,34,8],[880,6612],[101,4729],[603,9322],[69],[22],[603,7599],[113],[235,9076],[199,5712],[391,5647],[325,4503],[590,8147],[594,7070],[816,7608],[686,9579],[486],[243,5442],[379,7469],[139,4416,2044,48,8],[105],[483,2744],[54,6390],[199,8565],[39,2659],[371,3121],[146,9528],[248,4937],[83,6267],[199,7522],[112,3658],[663,4625,1415,69,2],[520,6642],[108,7804],[493,3296],[839,3868],[543,3073],[742,3135],[349,9745],[177,6935],[379,8959],[644,4746,1063,41,1],[409,4225],[498,9731],[296,7985],[126,4762],[662],[603,3359],[754,8407],[36,8480],[393,3967,1824,39,10],[243,2272],[172,9688],[22,6042],[121,5482],[391,8219],[470],[112,2084],[590,5855],[506,5999],[112,2373],[422,2217],[146,8645],[663],[800,4307],[603,10000],[520,8065],[613,7255],[669,7007],[525,5930],[437],[199,4754],[393],[608],[669,7860],[888,2574],[597,7790],[603,6062],[384,8881],[225,4576,1419,38,7],[270,4099],[498,3394],[379,8688],[771,7753],[311,6991],[248,4468],[172,4313],[73,2094],[225],[529,2462],[512,7860],[529,5782],[798,4307],[132],[36,7286],[520,7378],[311,6613],[432,9331],[67,5245],[400,2836],[506,6227],[151,7551],[689,3696],[512,6252],[210,4266,1597,36,6],[68,2465],[669,6053],[615,5351,2167,68,4],[717,9498],[296,8987],[290,4919,2261,54,5],[839,8117],[457,5122,1309,79,8],[798,5032],[669,4341],[422,6655],[203,8906],[379,8473],[400,8197],[297,3716,1809,60,6],[491,3264],[325,2670],[371,8203],[669,5436],[42,3813,1877,43,9],[25,7861],[498,6202],[311,3495],[402,8562],[816,6945],[604,3671,1476,44,5],[439,2497],[172],[742,9281],[369,8622],[489],[857,4004],[786,4407,2152,75,4],[349,4889],[68,9820],[172,3009],[504,4892,1997,75,9],[409,9678],[839,7161],[668,8420],[296,8932],[808,2185],[472,3107],[146,8020],[159,4542,1007,63,4],[145,4779],[520,3985],[578,6229],[603,9676],[379,9686],[349,9366],[67,8324],[39,5079],[317,8433],[535,2060],[242,4291],[90,4917,1584,82,9],[400,7659],[38,3796,1239,67,1],[409,3875],[72,8618],[409,4088],[768,4049,1274,41,3],[60,5293,2491,80,2],[845,7007],[669,9365],[100,4146,1136,46,6],[379,4318],[432,9435],[794,4420],[664,6682],[768,8546],[347,4358,1147,47,6],[222,7701],[794,9410],[529,9595],[391,8248],[159],[688,9812],[515,3630,1506,37,3],[391,9876],[668,3738,1412,34,5],[95,4221],[342,7223],[601,8391],[529,9667],[529,7634],[647,4712,1856,51,2],[613,6449],[121,5487],[290],[50,5199],[815,9911],[42],[557,3613,1779,76,8],[540,4480,1419,69,7],[520,5703],[480,3633],[384,3874],[748,4988,1940,81,9],[659,9109],[497,9764],[638],[39,3887],[890,4451,2033,84,5],[152,4565],[826,3769,1802,57,8],[771,8563],[391,6106],[855,4898,1540,64,10],[839,5043],[371,6944],[125,9890],[768,5567],[506,7960],[493,5006],[756],[566,4261],[493,8329],[597,6257],[457],[597,6178],[717,2818],[400,4478],[199,4108],[243,3844],[529],[664,4957],[433,4591],[480,5211,2365,41,6],[371,8770],[863,5229,1268,68,8],[222,5681],[108,2057],[247,5127,1545,35,1],[296,3396],[672,5345],[48,6943],[371,2725],[229,3921,1441,60,3],[689,2974],[261,7162],[68,4188],[67,9209],[68,3948],[255,5406,1181,84,2],[289,7930],[429,4795,1871,36,10],[562,6549],[689,8437],[261,3620,1782,38,8],[767,3611,1352,44,5],[880,9132],[289,2465],[460,6940],[493,7573],[872,9254],[67,6712],[778,5302,1394,61,3],[712],[237,4117,1473,83,4],[480,2766],[370,4451,1274,40,10],[688,7977],[178,3950],[808,9102],[244,5095,1339,42,10],[686,3609],[68,9364],[857,5602],[382,9921],[88,4257,1944,73,5],[845,5860],[855],[815,8640],[152,4893,1467,45,9],[422,2124],[126,6433],[370,2674],[631,4789,2325,48,6],[391,4725],[235,2733],[349,5411],[382,2769],[529,3566],[664,9951],[439,5195],[646,4775,1380,79,3],[146,5238],[590,8650],[460,2124],[95,5586],[68,2945],[614,5172,1169,72,3],[73,3922,1575,75,10],[480,7465],[162,4556,1071,82,10],[506,6745],[606,6798],[174,9757],[110,3738,1051,34,5],[633,6225],[498,3500],[768,8346],[328,8907],[839,7372],[145,9610],[69,5618],[325,4559,1812,78,2],[603,7140],[328,9879],[884,5386,1100,82,10],[20,5356,1189,85,5],[480],[311,8344],[533,7876],[66,4341],[50,5164],[126,7647],[538,4752,2039,41,6],[763,5113,1236,48,7],[145,5331],[695],[506,8813],[697,5148,2036,57,10],[418,4119,1994,49,2],[397,4387,2136,39,7],[796,4278,1899,54,1],[450,9735],[328,9238],[418],[73,2542],[108,8865],[780,5025,2272,85,8],[50,9649],[880,9183],[491,3425],[432,3978],[450,3646],[639],[450,4446],[748],[371,8280],[112,9454],[617,9696],[667,5009,1515,79,4],[180,4354,1243,84,2],[55,3915],[5,7938],[808,5479],[669,9145],[865,6080],[350,8747],[272,2594],[323,5271,1701,79,4],[349,8305],[543,3944],[491,2390],[101,6403],[212,6844],[730,3851,1064,35,8],[879,4627,1568,76,1],[450,3392],[302,3992,1981,64,9],[374,2701],[264,2560],[754,6075],[493,5049],[323,3684],[242,9247],[846,5170],[535,5099],[242,6298],[72,8325],[180],[325,6749],[772,6737],[268,6369],[422,5440],[594,8832],[888,3662],[374,9078],[848,8022],[777,5665],[772,7905],[349,3330],[882],[102,7103],[483,5413],[298,3975,1030,38,7],[669,2369],[603,7283],[110],[151,7367],[768,8510],[350,9013],[33,4471,1157,68,1],[433,9063],[688,2220],[112,6794],[67,6731],[152,3909],[235,6965],[447],[210],[374,5530],[402,4940],[409,6683],[535,7427],[409,3663],[264,8951],[410,4509,2065,62,6],[668,6630],[796],[48,2739],[317,5214,1833,58,7],[237],[361,5111],[177,8842],[820,8414],[359,4220,2015,37,5],[491,6438],[226,3056],[102,9007],[177,2684],[172,7961],[844,3781,1049,43,2],[543,6332],[270,5426],[677],[102,5557],[472,2668],[317,5390],[54,8349],[857,9625],[22,3970],[669,6924],[543,5477],[535,8721],[483,4641],[265,5752],[9,3694],[340,3886],[783,9420],[174,3898],[172,2608],[289,7580],[768,2990],[125,6367],[199,6910],[669,4802],[730],[667],[623,5071,1307,73,7],[235,9733],[261],[272,8917],[798,9297]]

'''



