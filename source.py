def f_3fc2849(a,b,c,d,e,f):
    return (a*b-c*d*e-f)%10
def f_404f934(a,b,c):
    return (a*b*c+f_3fc2849(a,b,c,795,8,396))%10
def f_4829a46(a,b):
    return (a*b+f_404f934(a,b,245)+f_3fc2849(a,b,164,482,679,900))%10
def f_5e65c19(a,b,c):
    return (a-b-c+f_404f934(a,b,c))%10
def f_3e77575(a,b,c,d,e,f,g,h,i,j):
    return (a*b+c*d-e*f-g+h+i+j+f_404f934(a,b,c)+f_404f934(a,b,c))%10
def f_11e6a4f(a,b,c,d,e,f):
    return (a-b-c-d-e+f+f_4829a46(a,b)+f_4829a46(a,b)+f_3fc2849(a,b,c,d,e,f))%10
def f_276f04f(a,b,c,d):
    return (a-b*c*d+f_3fc2849(a,b,c,d,520,699)+f_11e6a4f(a,b,c,d,959,507)+f_4829a46(a,b))%10
def f_44bbc00(a,b,c,d,e,f,g,h,i,j):
    return (a-b+c+d+e-f*g-h-i+j+f_404f934(a,b,c)+f_11e6a4f(a,b,c,d,e,f)+f_276f04f(a,b,c,d))%10
def f_323e173(a,b,c,d,e,f,g,h):
    return (a*b-c*d+e*f-g+h+f_4829a46(a,b)+f_44bbc00(a,b,c,d,e,f,g,h,181,670)+f_276f04f(a,b,c,d))%10
def f_10a1d56(a):
    return (a+f_404f934(a,111,188))%10
def f_1537206(a,b,c,d,e,f):
    return (a+b+c-d*e+f+f_44bbc00(a,b,c,d,e,f,188,162,484,148))%10
def f_1543215(a,b,c):
    return (a*b*c+f_10a1d56(a)+f_44bbc00(a,b,c,818,340,752,392,516,415,260)+f_11e6a4f(a,b,c,238,530,556))%10
def f_70450f(a,b):
    return (a-b+f_4829a46(a,b))%10
def f_21e3b2e(a,b,c,d,e,f,g,h):
    return (a*b-c-d+e*f-g*h+f_276f04f(a,b,c,d)+f_11e6a4f(a,b,c,d,e,f)+f_5e65c19(a,b,c))%10
def f_3179eb1(a,b,c,d,e,f,g,h,i):
    return (a+b+c*d*e+f-g+h+i+f_4829a46(a,b)+f_404f934(a,b,c))%10
def f_5d6c325(a,b,c):
    return (a*b-c+f_3e77575(a,b,c,315,576,486,967,184,2,338)+f_70450f(a,b)+f_323e173(a,b,c,475,446,859,898,485))%10
def f_3baeede(a,b,c,d,e,f,g,h,i):
    return (a*b*c-d+e-f+g+h+i+f_3179eb1(a,b,c,d,e,f,g,h,i)+f_44bbc00(a,b,c,d,e,f,g,h,i,335)+f_3fc2849(a,b,c,d,e,f))%10
def f_60d002(a,b,c):
    return (a+b+c+f_11e6a4f(a,b,c,505,283,95)+f_3e77575(a,b,c,231,536,582,911,319,606,57))%10
def f_982326(a,b):
    return (a-b+f_1543215(a,b,550)+f_3e77575(a,b,48,38,333,831,333,905,226,411))%10
def f_516909d(a,b,c,d):
    return (a*b*c*d+f_276f04f(a,b,c,d)+f_21e3b2e(a,b,c,d,456,891,598,573)+f_5e65c19(a,b,c))%10
def f_434092a(a,b,c,d,e,f,g,h,i,j):
    return (a-b*c+d-e+f+g*h*i+j+f_5e65c19(a,b,c)+f_516909d(a,b,c,d)+f_5d6c325(a,b,c))%10
def f_95c5a4(a,b):
    return (a*b+f_434092a(a,b,565,793,600,255,136,291,472,773)+f_11e6a4f(a,b,155,641,756,593))%10
def f_1c44cb0(a,b,c,d,e,f,g,h,i):
    return (a-b+c-d-e+f-g-h-i+f_3179eb1(a,b,c,d,e,f,g,h,i)+f_3e77575(a,b,c,d,e,f,g,h,i,737)+f_44bbc00(a,b,c,d,e,f,g,h,i,719))%10
def f_1ce677a(a,b,c):
    return (a+b+c+f_323e173(a,b,c,512,416,313,964,3)+f_516909d(a,b,c,633)+f_5e65c19(a,b,c))%10
def f_521625(a,b,c):
    return (a-b-c+f_982326(a,b)+f_516909d(a,b,c,83)+f_3e77575(a,b,c,632,28,367,275,684,109,746))%10
def f_154f682(a,b,c,d,e,f,g):
    return (a-b*c-d+e-f-g+f_404f934(a,b,c)+f_3fc2849(a,b,c,d,e,f)+f_3179eb1(a,b,c,d,e,f,g,163,617))%10
def f_2b14842(a,b,c,d,e):
    return (a-b*c+d+e+f_10a1d56(a)+f_1537206(a,b,c,d,e,321)+f_4829a46(a,b))%10
def f_267eeba(a,b,c,d,e,f,g,h,i):
    return (a-b*c*d-e-f*g*h*i+f_10a1d56(a))%10
def f_943895(a,b,c,d,e,f,g,h,i,j):
    return (a+b*c-d-e-f-g*h-i-j+f_5e65c19(a,b,c)+f_3e77575(a,b,c,d,e,f,g,h,i,j)+f_521625(a,b,c))%10
def f_4561101(a,b,c,d,e,f,g,h,i):
    return (a-b+c+d-e-f+g*h*i+f_44bbc00(a,b,c,d,e,f,g,h,i,47)+f_44bbc00(a,b,c,d,e,f,g,h,i,147))%10
def f_2d2e151(a):
    return (a+f_1c44cb0(a,211,154,183,863,523,171,643,100))%10
def f_5db3fab(a,b,c,d,e):
    return (a+b+c-d*e+f_1543215(a,b,c)+f_521625(a,b,c))%10
def f_4b80977(a,b,c,d,e,f):
    return (a-b*c-d+e-f+f_276f04f(a,b,c,d)+f_4561101(a,b,c,d,e,f,259,152,779))%10
def f_25fb1da(a,b,c,d,e,f,g):
    return (a*b+c*d-e*f+g+f_3e77575(a,b,c,d,e,f,g,671,573,64)+f_1543215(a,b,c))%10
def f_dfc6ca(a,b,c):
    return (a+b+c+f_982326(a,b))%10
def f_f79bd0(a,b,c,d,e,f,g,h,i,j):
    return (a+b-c*d*e+f*g*h-i+j+f_2b14842(a,b,c,d,e))%10
def f_4daee6(a):
    return (a+f_1c44cb0(a,928,870,93,587,425,416,271,747))%10
def f_496990b(a,b,c,d,e):
    return (a-b+c+d+e+f_404f934(a,b,c))%10
def f_5b6d309(a,b):
    return (a-b+f_1543215(a,b,539)+f_1ce677a(a,b,797)+f_1c44cb0(a,b,211,509,871,106,874,536,397))%10
def f_4aecd47(a,b,c,d,e,f,g,h):
    return (a-b*c-d*e-f+g+h+f_276f04f(a,b,c,d))%10
def f_3d93229(a,b,c,d):
    return (a-b*c+d+f_1ce677a(a,b,c)+f_404f934(a,b,c))%10
def f_1d21f7d(a,b,c,d,e,f,g,h,i):
    return (a+b*c-d*e+f+g*h-i+f_323e173(a,b,c,d,e,f,g,h)+f_3e77575(a,b,c,d,e,f,g,h,i,294)+f_3d93229(a,b,c,d))%10
def f_270f3be(a):
    return (a+f_4b80977(a,387,976,27,654,588)+f_25fb1da(a,414,415,117,8,889,663))%10
def f_5c56b8b(a,b,c):
    return (a+b*c+f_11e6a4f(a,b,c,379,258,45)+f_95c5a4(a,b)+f_323e173(a,b,c,779,254,317,499,649))%10
def f_43b5b8c(a,b,c,d,e,f,g):
    return (a*b+c+d+e*f-g+f_dfc6ca(a,b,c)+f_5c56b8b(a,b,c)+f_f79bd0(a,b,c,d,e,f,g,318,331,144))%10
def f_2038f07(a,b,c,d,e,f,g,h,i):
    return (a*b+c*d+e-f*g*h-i+f_276f04f(a,b,c,d)+f_3fc2849(a,b,c,d,e,f)+f_21e3b2e(a,b,c,d,e,f,g,h))%10
def f_513f75a(a,b,c,d,e,f):
    return (a+b+c-d-e-f+f_43b5b8c(a,b,c,d,e,f,760)+f_4daee6(a)+f_434092a(a,b,c,d,e,f,972,63,931,735))%10
def f_5b915db(a,b,c,d,e,f):
    return (a+b-c-d*e-f+f_154f682(a,b,c,d,e,f,124))%10
def f_4685338(a,b,c,d,e,f,g,h,i):
    return (a+b+c-d+e+f+g+h-i+f_1543215(a,b,c)+f_10a1d56(a))%10
def f_4219d3d(a,b,c,d,e,f,g,h,i):
    return (a+b*c-d-e-f+g+h*i+f_4aecd47(a,b,c,d,e,f,g,h))%10
def f_2d2468e(a,b,c,d,e):
    return (a+b+c+d+e+f_2b14842(a,b,c,d,e)+f_496990b(a,b,c,d,e)+f_11e6a4f(a,b,c,d,e,291))%10
def f_2980ac2(a,b,c,d,e):
    return (a*b+c*d*e+f_3179eb1(a,b,c,d,e,692,428,848,728)+f_5d6c325(a,b,c)+f_4daee6(a))%10
def f_3db47ef(a,b,c,d):
    return (a*b*c-d+f_3fc2849(a,b,c,d,901,974)+f_267eeba(a,b,c,d,358,607,314,270,117))%10
def f_29beb15(a,b,c):
    return (a*b-c+f_43b5b8c(a,b,c,74,633,468,579)+f_2d2468e(a,b,c,811,996)+f_513f75a(a,b,c,29,697,916))%10
def f_e17983(a,b):
    return (a*b+f_25fb1da(a,b,106,737,297,834,753)+f_1c44cb0(a,b,482,502,894,841,589,191,175))%10
def f_328ab5b(a,b,c,d,e,f,g,h,i):
    return (a*b*c*d-e*f*g+h+i+f_1537206(a,b,c,d,e,f))%10
def f_2118f76(a,b,c,d,e,f,g,h,i):
    return (a*b*c-d+e*f*g-h+i+f_3d93229(a,b,c,d)+f_943895(a,b,c,d,e,f,g,h,i,213)+f_513f75a(a,b,c,d,e,f))%10
def f_1026acb(a,b):
    return (a*b+f_4aecd47(a,b,682,979,91,181,468,330)+f_521625(a,b,863))%10
def f_5eec931(a,b,c):
    return (a+b+c+f_e17983(a,b)+f_521625(a,b,c))%10
def f_4ef43d8(a):
    return (a+f_4685338(a,939,575,609,755,167,70,703,541)+f_2980ac2(a,971,828,710,372))%10
def f_48876b1(a,b,c,d,e):
    return (a*b*c-d-e+f_328ab5b(a,b,c,d,e,687,252,243,399)+f_5c56b8b(a,b,c))%10
def f_dc3902(a,b,c,d,e,f,g,h,i,j):
    return (a+b*c+d-e-f*g+h*i+j+f_1ce677a(a,b,c)+f_1c44cb0(a,b,c,d,e,f,g,h,i))%10
def f_385ec(a,b,c,d,e,f,g,h):
    return (a*b+c*d-e+f+g+h+f_3179eb1(a,b,c,d,e,f,g,h,928)+f_404f934(a,b,c)+f_404f934(a,b,c))%10
def f_99b8eb(a,b,c,d):
    return (a-b+c*d+f_44bbc00(a,b,c,d,494,175,234,761,38,945))%10
def f_33d1eb4(a,b,c,d,e,f,g):
    return (a-b-c+d+e-f+g+f_1d21f7d(a,b,c,d,e,f,g,904,948)+f_4aecd47(a,b,c,d,e,f,g,459)+f_1026acb(a,b))%10
def f_1a4f4e5(a,b,c,d):
    return (a*b*c+d+f_4aecd47(a,b,c,d,222,402,880,448)+f_434092a(a,b,c,d,743,339,981,199,664,86))%10
def f_531a91b(a,b):
    return (a*b+f_2d2468e(a,b,780,884,909)+f_5e65c19(a,b,755)+f_95c5a4(a,b))%10
def f_1a5d76b(a):
    return (a+f_e17983(a,682)+f_f79bd0(a,911,947,778,697,35,875,264,226,310))%10
def f_1df309(a,b,c,d,e,f,g):
    return (a*b*c+d+e-f+g+f_70450f(a,b))%10
def f_14d0721(a,b,c,d,e,f,g,h,i):
    return (a-b+c*d*e*f-g*h*i+f_4ef43d8(a)+f_2d2468e(a,b,c,d,e))%10
def f_42b43a6(a,b,c,d,e,f,g,h):
    return (a*b*c-d*e-f+g-h+f_43b5b8c(a,b,c,d,e,f,g)+f_2038f07(a,b,c,d,e,f,g,h,33)+f_3fc2849(a,b,c,d,e,f))%10
def f_26b5f98(a,b,c,d,e,f,g,h,i,j):
    return (a*b+c*d-e*f+g*h*i*j+f_385ec(a,b,c,d,e,f,g,h)+f_5d6c325(a,b,c))%10
def f_3b71344(a,b,c,d,e,f,g,h):
    return (a*b+c+d*e-f-g+h+f_f79bd0(a,b,c,d,e,f,g,h,449,233))%10
def f_27e5639(a,b,c,d,e,f,g):
    return (a-b-c-d*e*f*g+f_531a91b(a,b)+f_2980ac2(a,b,c,d,e))%10
def f_91596(a):
    return (a+f_2118f76(a,982,165,659,502,50,541,484,274))%10
def f_30c3354(a,b,c,d,e,f):
    return (a-b*c*d*e*f+f_33d1eb4(a,b,c,d,e,f,917))%10
def f_4b32a8a(a,b,c,d,e,f):
    return (a*b*c*d+e+f+f_385ec(a,b,c,d,e,f,953,474))%10
def f_19797f(a,b,c,d):
    return (a*b+c-d+f_91596(a)+f_21e3b2e(a,b,c,d,591,344,208,290)+f_323e173(a,b,c,d,195,155,55,46))%10
def f_461efc8(a,b,c,d,e,f,g,h):
    return (a*b-c-d*e-f+g-h+f_e17983(a,b)+f_531a91b(a,b)+f_99b8eb(a,b,c,d))%10
def f_2a6382f(a,b,c,d,e,f,g,h,i,j):
    return (a-b+c+d*e*f-g+h-i+j+f_3179eb1(a,b,c,d,e,f,g,h,i))%10
def f_1ced336(a,b,c,d,e):
    return (a+b-c-d-e+f_516909d(a,b,c,d))%10
def f_4eb2186(a,b):
    return (a+b+f_29beb15(a,b,872))%10
def f_315996e(a,b,c):
    return (a-b-c+f_3fc2849(a,b,c,836,318,119)+f_44bbc00(a,b,c,600,35,775,264,532,381,379))%10
def f_4d0a9a0(a,b,c,d,e,f,g):
    return (a*b-c-d-e+f-g+f_5db3fab(a,b,c,d,e)+f_1d21f7d(a,b,c,d,e,f,g,165,920)+f_323e173(a,b,c,d,e,f,g,475))%10
def f_5146ecb(a,b,c,d,e,f,g):
    return (a+b+c+d*e*f-g+f_4685338(a,b,c,d,e,f,g,732,166)+f_4829a46(a,b)+f_521625(a,b,c))%10
def f_2312b67(a,b,c,d,e,f,g,h,i):
    return (a*b*c*d*e-f+g*h*i+f_1df309(a,b,c,d,e,f,g)+f_323e173(a,b,c,d,e,f,g,h))%10
def f_4fe1fea(a,b,c,d,e,f,g):
    return (a*b-c*d*e+f-g+f_14d0721(a,b,c,d,e,f,g,183,346)+f_19797f(a,b,c,d))%10
def f_e73849(a,b,c,d):
    return (a+b-c+d+f_5c56b8b(a,b,c)+f_26b5f98(a,b,c,d,237,764,815,332,457,45))%10
def f_3602881(a,b,c,d,e,f):
    return (a*b+c+d*e+f+f_1c44cb0(a,b,c,d,e,f,581,217,466)+f_404f934(a,b,c)+f_434092a(a,b,c,d,e,f,872,991,345,185))%10
def f_1399b76(a,b):
    return (a*b+f_5146ecb(a,b,470,210,26,350,872)+f_385ec(a,b,288,595,950,128,897,141))%10
def f_312a318(a,b,c,d,e,f):
    return (a*b-c+d*e-f+f_25fb1da(a,b,c,d,e,f,954)+f_3e77575(a,b,c,d,e,f,637,137,224,441))%10
def f_3ee3b81(a,b,c,d,e,f):
    return (a*b*c-d*e*f+f_25fb1da(a,b,c,d,e,f,166))%10
def f_90c07b(a,b,c,d,e):
    return (a*b-c-d+e+f_95c5a4(a,b)+f_dfc6ca(a,b,c)+f_33d1eb4(a,b,c,d,e,236,767))%10
def f_3901b28(a,b,c,d,e,f,g,h):
    return (a*b+c-d*e*f-g+h+f_1026acb(a,b)+f_5146ecb(a,b,c,d,e,f,g)+f_1d21f7d(a,b,c,d,e,f,g,h,317))%10
def f_325d499(a,b):
    return (a+b+f_43b5b8c(a,b,884,830,508,114,421)+f_1399b76(a,b)+f_4fe1fea(a,b,11,737,255,722,782))%10
def f_5e6c9d6(a,b,c,d,e,f,g,h):
    return (a-b+c*d*e+f*g-h+f_982326(a,b)+f_323e173(a,b,c,d,e,f,g,h)+f_3901b28(a,b,c,d,e,f,g,h))%10
def f_2e3073c(a,b,c,d,e,f,g,h,i,j):
    return (a+b*c*d+e*f*g+h*i-j+f_5c56b8b(a,b,c))%10
def f_23c61d8(a,b,c,d,e,f,g,h,i):
    return (a+b-c+d*e*f-g-h*i+f_91596(a))%10
def f_1e0f2ac(a,b,c,d,e):
    return (a*b+c-d-e+f_154f682(a,b,c,d,e,22,8))%10
def f_342de1c(a,b,c):
    return (a*b*c+f_11e6a4f(a,b,c,573,112,823)+f_315996e(a,b,c))%10
def f_3d5149e(a,b,c,d,e,f,g,h,i,j):
    return (a*b-c-d-e*f*g+h*i-j+f_1ced336(a,b,c,d,e)+f_982326(a,b))%10
def f_313e9b5(a,b,c,d):
    return (a*b+c*d+f_1ced336(a,b,c,d,280)+f_3b71344(a,b,c,d,722,166,630,390)+f_4fe1fea(a,b,c,d,721,952,217))%10
def f_5a33a53(a,b):
    return (a+b+f_26b5f98(a,b,142,152,992,684,885,86,952,196)+f_4daee6(a))%10
def f_1ca99e6(a,b,c,d,e,f,g,h,i,j):
    return (a-b-c-d-e+f-g*h+i*j+f_26b5f98(a,b,c,d,e,f,g,h,i,j)+f_4d0a9a0(a,b,c,d,e,f,g))%10
def f_b8a492(a,b,c,d,e,f,g,h,i):
    return (a*b-c-d-e-f+g*h+i+f_48876b1(a,b,c,d,e)+f_30c3354(a,b,c,d,e,f)+f_4fe1fea(a,b,c,d,e,f,g))%10
def f_5cff6dd(a,b,c,d,e,f):
    return (a-b*c+d+e-f+f_5146ecb(a,b,c,d,e,f,807)+f_2312b67(a,b,c,d,e,f,896,499,696))%10
def f_4f47e84(a,b,c,d,e,f,g,h,i,j):
    return (a*b+c+d-e+f-g*h*i*j+f_1537206(a,b,c,d,e,f)+f_43b5b8c(a,b,c,d,e,f,g)+f_95c5a4(a,b))%10
def f_3f26d4f(a,b,c,d,e,f,g):
    return (a*b-c+d-e-f*g+f_99b8eb(a,b,c,d)+f_5eec931(a,b,c))%10
def f_6ad18c(a,b,c):
    return (a*b+c+f_521625(a,b,c))%10
def f_1ba6eba(a,b,c,d,e,f,g):
    return (a*b*c-d*e+f*g+f_3602881(a,b,c,d,e,f)+f_4219d3d(a,b,c,d,e,f,g,986,631))%10
def f_17a71e9(a,b,c,d,e,f,g,h,i,j):
    return (a-b+c*d+e-f+g+h+i+j+f_3ee3b81(a,b,c,d,e,f)+f_29beb15(a,b,c)+f_4829a46(a,b))%10
def f_3370a3a(a,b,c,d):
    return (a+b-c+d+f_4daee6(a)+f_1ce677a(a,b,c)+f_2980ac2(a,b,c,d,104))%10
def f_1adec04(a,b,c):
    return (a*b-c+f_270f3be(a)+f_313e9b5(a,b,c,457)+f_1c44cb0(a,b,c,225,553,110,57,690,816))%10
def f_3e8aba5(a,b,c,d):
    return (a-b*c*d+f_2d2468e(a,b,c,d,336)+f_4219d3d(a,b,c,d,541,176,338,563,603))%10
def f_58bc2(a,b,c,d):
    return (a-b-c-d+f_2d2e151(a)+f_1a4f4e5(a,b,c,d)+f_3901b28(a,b,c,d,793,343,534,372))%10
def f_1b33739(a,b,c,d,e,f):
    return (a+b*c-d+e+f+f_60d002(a,b,c)+f_3901b28(a,b,c,d,e,f,621,288)+f_3901b28(a,b,c,d,e,f,382,984))%10
def f_33e0fde(a,b):
    return (a-b+f_434092a(a,b,57,251,907,397,249,477,178,399)+f_1537206(a,b,71,338,63,134))%10
def f_43b6a1e(a,b,c,d,e,f,g,h):
    return (a+b+c*d+e+f*g+h+f_4829a46(a,b)+f_2d2e151(a)+f_1df309(a,b,c,d,e,f,g))%10
def f_5edabd1(a,b,c,d,e,f,g,h,i):
    return (a-b-c*d+e-f+g-h*i+f_6ad18c(a,b,c)+f_4b32a8a(a,b,c,d,e,f)+f_2980ac2(a,b,c,d,e))%10
def f_5809bdc(a,b,c):
    return (a*b*c+f_6ad18c(a,b,c)+f_4ef43d8(a))%10
def f_3a65141(a,b,c,d,e,f):
    return (a*b-c+d+e-f+f_4685338(a,b,c,d,e,f,934,408,609)+f_3d93229(a,b,c,d))%10
def f_1a4a712(a,b):
    return (a*b+f_4685338(a,b,499,866,984,782,209,158,818)+f_91596(a)+f_404f934(a,b,423))%10
def f_50fb1b3(a,b,c,d,e,f,g):
    return (a*b*c*d*e*f*g+f_404f934(a,b,c)+f_4ef43d8(a)+f_dc3902(a,b,c,d,e,f,g,343,524,30))%10
def f_2bbc1b(a,b,c,d,e,f,g):
    return (a-b+c*d*e+f*g+f_1a5d76b(a))%10
def f_4dd8575(a,b,c,d,e):
    return (a*b-c+d-e+f_276f04f(a,b,c,d)+f_516909d(a,b,c,d))%10
def f_416ec8a(a,b,c,d,e,f):
    return (a*b*c*d+e+f+f_3e8aba5(a,b,c,d))%10
def f_e1680c(a,b):
    return (a+b+f_5eec931(a,b,102))%10
def f_40dda3b(a,b,c,d,e,f,g,h):
    return (a+b+c+d*e*f-g-h+f_416ec8a(a,b,c,d,e,f)+f_30c3354(a,b,c,d,e,f))%10
def f_22ec421(a,b,c,d,e,f):
    return (a-b-c*d-e-f+f_10a1d56(a)+f_11e6a4f(a,b,c,d,e,f))%10
def f_4a02c54(a,b,c,d,e):
    return (a+b-c-d*e+f_22ec421(a,b,c,d,e,37)+f_17a71e9(a,b,c,d,e,669,313,17,109,97)+f_313e9b5(a,b,c,d))%10
def f_236ac1(a,b,c,d):
    return (a+b-c-d+f_1399b76(a,b)+f_315996e(a,b,c)+f_3901b28(a,b,c,d,564,345,282,988))%10
def f_38f59d6(a,b):
    return (a*b+f_1c44cb0(a,b,361,431,410,227,153,972,802)+f_154f682(a,b,87,323,260,47,564)+f_21e3b2e(a,b,522,420,490,978,638,584))%10
def f_599d433(a,b,c,d,e):
    return (a-b+c*d*e+f_2d2e151(a))%10
def f_e99203(a,b,c):
    return (a*b-c+f_4aecd47(a,b,c,34,101,682,40,187))%10
def f_488a2c0(a,b,c):
    return (a-b+c+f_4a02c54(a,b,c,962,302))%10
def f_15a3573(a,b,c,d,e,f,g):
    return (a*b*c*d-e-f*g+f_1c44cb0(a,b,c,d,e,f,g,296,276)+f_513f75a(a,b,c,d,e,f))%10
def f_31f6789(a,b,c,d,e,f,g,h,i,j):
    return (a*b*c+d+e-f+g-h*i+j+f_4aecd47(a,b,c,d,e,f,g,h))%10
def f_2d34b7f(a,b,c,d,e,f,g,h,i,j):
    return (a+b+c+d-e-f-g-h-i-j+f_325d499(a,b))%10
def f_3c823f9(a,b,c,d):
    return (a-b*c+d+f_2980ac2(a,b,c,d,888)+f_1e0f2ac(a,b,c,d,528)+f_4aecd47(a,b,c,d,195,656,48,677))%10
def f_5b1da69(a,b,c,d,e):
    return (a*b+c*d+e+f_5a33a53(a,b))%10
def f_38c990e(a,b,c):
    return (a-b*c+f_4b80977(a,b,c,784,787,816))%10
def f_3af46d9(a,b,c,d,e,f,g,h):
    return (a-b*c-d+e+f+g-h+f_342de1c(a,b,c))%10
def f_236051d(a,b):
    return (a+b+f_599d433(a,b,742,392,985)+f_2d34b7f(a,b,319,652,599,66,208,458,940,84)+f_43b6a1e(a,b,456,246,115,411,997,133))%10
def f_1132978(a):
    return (a+f_513f75a(a,796,182,411,294,526)+f_70450f(a,566)+f_30c3354(a,729,623,447,147,613))%10
def f_5b18084(a,b,c,d,e,f,g,h,i,j):
    return (a+b-c*d*e*f-g+h-i-j+f_3602881(a,b,c,d,e,f))%10
def f_1185c60(a,b,c,d,e,f,g,h):
    return (a*b+c-d-e-f+g+h+f_1132978(a)+f_e1680c(a,b)+f_516909d(a,b,c,d))%10
def f_17f9f37(a,b,c,d,e,f,g,h,i):
    return (a-b-c-d*e-f+g+h+i+f_6ad18c(a,b,c)+f_4eb2186(a,b)+f_b8a492(a,b,c,d,e,f,g,h,i))%10
def f_3bb6116(a,b,c,d,e,f,g,h):
    return (a*b*c-d*e-f*g-h+f_40dda3b(a,b,c,d,e,f,g,h))%10
def f_58e02bf(a,b,c,d,e,f):
    return (a*b-c-d*e+f+f_2bbc1b(a,b,c,d,e,f,526))%10
def f_1df4418(a,b,c,d,e,f,g):
    return (a*b-c+d-e+f*g+f_1adec04(a,b,c)+f_5e65c19(a,b,c)+f_315996e(a,b,c))%10
def f_271d934(a,b,c,d,e,f,g):
    return (a*b+c-d*e-f+g+f_5a33a53(a,b)+f_1132978(a)+f_323e173(a,b,c,d,e,f,g,123))%10
def f_5c62d79(a,b,c,d,e,f):
    return (a*b-c+d+e-f+f_22ec421(a,b,c,d,e,f)+f_4b80977(a,b,c,d,e,f))%10
def f_574b9d(a,b,c,d,e):
    return (a*b-c-d*e+f_43b6a1e(a,b,c,d,e,734,390,695)+f_267eeba(a,b,c,d,e,83,206,618,977))%10
def f_1f3c995(a,b,c,d,e,f,g,h):
    return (a*b-c-d*e+f*g*h+f_14d0721(a,b,c,d,e,f,g,h,741)+f_1ba6eba(a,b,c,d,e,f,g))%10
def f_3941191(a,b,c,d,e,f,g,h):
    return (a+b*c-d-e-f*g+h+f_3a65141(a,b,c,d,e,f))%10
def f_5c08360(a,b,c,d):
    return (a+b*c+d+f_5809bdc(a,b,c)+f_5e6c9d6(a,b,c,d,550,39,88,13)+f_4daee6(a))%10
def f_4dfa0c1(a,b,c):
    return (a+b*c+f_4daee6(a)+f_1ce677a(a,b,c)+f_2d34b7f(a,b,c,314,213,7,640,302,765,145))%10
def f_2e3793d(a,b,c,d,e,f,g,h,i,j):
    return (a+b*c+d-e*f+g-h*i*j+f_43b6a1e(a,b,c,d,e,f,g,h)+f_f79bd0(a,b,c,d,e,f,g,h,i,j)+f_3db47ef(a,b,c,d))%10
def f_2f9c842(a,b,c,d,e):
    return (a*b*c*d+e+f_f79bd0(a,b,c,d,e,796,603,674,510,937)+f_99b8eb(a,b,c,d)+f_44bbc00(a,b,c,d,e,604,194,642,693,24))%10
