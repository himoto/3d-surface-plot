# Table S4A. Good fitting parameter sets for the initial mechanistic models.
# 7

F_P = [\
  'V1',
  'Km1',
  'V2',
  'Km2',
  'V3',
  'Km3',
  'V4',
  'Km4',
  'V5',
  'Km5',
  'V6',
  'Km6',
  'KimERK',
  'KexERK',
  'KimpERK',
  'KexpERK',
  'KimppERK',
  'KexppERK',
  'V10',
  'Km10',
  'n10',
  'p11',
  'p12',
  'p13',
  'V14',
  'Km14',
  'V15',
  'Km15',
  'p16',
  'p17',
  'KimDUSP',
  'KexDUSP',
  'KimpDUSP',
  'KexpDUSP',
  'V20',
  'Km20',
  'V21',
  'Km21',
  'p22',
  'p23',
  'V24',
  'Km24',
  'V25',
  'Km25',
  'KimRSK',
  'KexRSK',
  'V27',
  'Km27',
  'V28',
  'Km28',
  'V29',
  'Km29',
  'V30',
  'Km30',
  'V31',
  'Km31',
  'n31',
  'p32',
  'p33',
  'p34',
  'V35',
  'Km35',
  'V36',
  'Km36',
  'V37',
  'Km37',
  'p38',
  'p39',
  'KimFOS',
  'KexFOS',
  'KimpcFOS',
  'KexpcFOS',
  'V42',
  'Km42',
  'V43',
  'Km43',
  'V44',
  'Km44',
  'p45',
  'p46',
  'p47',
  'm47',
  'p48',
  'p49',
  'm49',
  'p50',
  'p51',
  'm51',
  'p52',
  'm52',
  'p53',
  'p54',
  'm54',
  'p55',
  'p56',
  'm56',
  'V57',
  'Km57',
  'n57',
  'p58',
  'p59',
  'p60',
  'p61',
  'KimF',
  'KexF',
  'p63',
  'KF31',
  'nF31',
  #
  'a',
  'Vn',
  'Vc',
  'Ligand',
  'EGF',
  'HRG'\
]

for i,name in enumerate(F_P):
  exec('%s=%d'%(name,i),globals())

def f_params():

  x = [0]*len(F_P)

  x[V1] = 1.915E-01
  x[Km1] = 8.482E+02
  x[V2] = 2.20e-01
  x[Km2] = 3.50e+02
  x[V3] = 7.20e-01
  x[Km3] = 1.60e+02
  x[V4] = 6.48e-01
  x[Km4] = 6.00e+01
  x[V5] = 2.079E+01
  x[Km5] = 7.889E-01
  x[V6] = x[V5]
  x[Km6] = x[Km5]
  x[KimERK] = 1.20e-02
  x[KexERK] = 1.80e-02
  x[KimpERK] = 1.20e-02
  x[KexpERK] = 1.80e-02
  x[KimppERK] = 1.10e-02
  x[KexppERK] = 1.30e-02
  x[V10] = 3.818E+00
  x[Km10] = 1.851E+01
  x[n10] = 3.804E+00
  x[p11] = 6.691E-05
  x[p12] = 2.860E-03
  x[p13] = 4.964E-03
  x[V14] = 4.003E+00
  x[Km14] = 6.255E+03
  x[V15] = 2.387E-01
  x[Km15] = 3.996E-03
  x[p16] = 2.57e-04
  x[p17] = 9.63e-05
  x[KimDUSP] = 1.084E-01
  x[KexDUSP] = 1.152E-02
  x[KimpDUSP] = x[KimDUSP]
  x[KexpDUSP] = x[KexDUSP]
  x[V20] = 9.758E-01
  x[Km20] = 3.256E+04
  x[V21] = 2.681E-02
  x[Km21] = 3.226E-02
  x[p22] = 2.57e-04
  x[p23] = 9.63e-05
  x[V24] = 1.270E+00
  x[Km24] = 9.900E+03
  x[V25] = 1.010E+02
  x[Km25] = 2.596E-02
  x[KimRSK] = 2.419E-01
  x[KexRSK] = 3.272E-02
  x[V27] = 2.177E+00
  x[Km27] = 4.366E+02
  x[V28] = 4.419E-01
  x[Km28] = 2.614E-02
  x[V29] = 8.875E-02
  x[Km29] = 2.325E+04
  x[V30] = 3.897E+00
  x[Km30] = 3.448E+02
  x[V31] = 4.601E+01
  x[Km31] = 4.475E+00
  x[n31] = 1.238E+00
  x[p32] = 1.464E-03
  x[p33] = 1.436E-03
  x[p34] = 1.132E-04
  x[V35] = 5.469E-02
  x[Km35] = 3.697E+04
  x[V36] = 1.405E+00
  x[Km36] = 4.027E+03
  x[V37] = 1.674E+01
  x[Km37] = 1.531E+02
  x[p38] = 2.57e-04
  x[p39] = 9.63e-05
  x[KimFOS] = 5.499E-01
  x[KexFOS] = 1.046E-01
  x[KimpcFOS] = x[KimFOS]
  x[KexpcFOS] = x[KexFOS]
  x[V42] = 4.465E+00
  x[Km42] = 2.075E+02
  x[V43] = 0.076717457
  x[Km43] = 2.191E+02
  x[V44] = 6.051E-01
  x[Km44] = 8.780E+02
  x[p45] = 2.57e-04
  x[p46] = 9.63e-05
  x[p47] = 1.505E-03
  x[m47] = 1.811E+01
  x[p48] = 7.106E-03
  x[p49] = 4.922E-01
  x[m49] = 2.006E-02
  x[p50] = 4.166E+00
  x[p51] = 2.579E-01
  x[m51] = 3.182E+02
  x[p52] = x[p47]
  x[m52] = x[m47]
  x[p53] = x[p48]
  x[p54] = x[p49]
  x[m54] = x[m49]
  x[p55] = x[p50]
  x[p56] = x[p51]
  x[m56] = x[m51]

  x[a] = 3.278E+02
  x[Vn] = 0.22
  x[Vc] = 0.94

  x[EGF]= 0
  x[HRG]= 1

  return x