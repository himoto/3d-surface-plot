import matplotlib.pyplot as plt
exp = ExperimentalData()

plt.figure(figsize=(20,8))
plt.rcParams['font.size'] = 16
plt.rcParams['font.family'] = 'Arial'
plt.rcParams['axes.linewidth'] = 2
plt.rcParams['lines.linewidth'] = 2.5
plt.rcParams['lines.markersize'] = 10

plt.subplots_adjust(wspace=0.5, hspace=0.5)

plt.subplot(2,4,1)
e = plt.errorbar(exp.t2/60.,exp.egf_MEKc_av,yerr=exp.egf_MEKc_se,lw=1,
    markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(exp.t2/60.,exp.hrg_MEKc_av,yerr=exp.hrg_MEKc_se,lw=1,
    markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.plot(t,PMEK_cyt[:,0],'b',label='EGF')
plt.plot(t,PMEK_cyt[:,1],'r',label='HRG')
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel('Phosphorylated MEK\n(cytoplasm)')

plt.subplot(2,4,2)
e = plt.errorbar(exp.t2/60.,exp.egf_ERKc_av,yerr=exp.egf_ERKc_se,lw=1,
    markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(exp.t2/60.,exp.hrg_ERKc_av,yerr=exp.hrg_ERKc_se,lw=1,
    markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.plot(t,PERK_cyt[:,0]/np.max(PERK_cyt[:,1]),'b')
plt.plot(t,PERK_cyt[:,1]/np.max(PERK_cyt[:,1]),'r')
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel('Phosphorylated ERK\n(cytoplasm)')

plt.subplot(2,4,3)
e = plt.errorbar(exp.t2/60.,exp.egf_RSKw_av,yerr=exp.egf_RSKw_se,lw=1,
    markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(exp.t2/60.,exp.hrg_RSKw_av,yerr=exp.hrg_RSKw_se,lw=1,
    markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.plot(t,PRSK_wcl[:,0]/np.max(PRSK_wcl[:,1]),'b')
plt.plot(t,PRSK_wcl[:,1]/np.max(PRSK_wcl[:,1]),'r')
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel('Phosphorylated RSK\n(whole cell)')

plt.subplot(2,4,4)
e = plt.errorbar(exp.t3/60.,exp.egf_CREBw_av,yerr=exp.egf_CREBw_se,lw=1,
    markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(exp.t3/60.,exp.hrg_CREBw_av,yerr=exp.hrg_CREBw_se,lw=1,
    markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.plot(t,PCREB_wcl[:,0]/np.max(PCREB_wcl[:,1]),'b')
plt.plot(t,PCREB_wcl[:,1]/np.max(PCREB_wcl[:,1]),'r')
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel('Phosphorylated CREB\n(whole cell)')

plt.subplot(2,4,5)
e = plt.errorbar(exp.t5/60.,exp.egf_DUSPmRNA_av,yerr=exp.egf_DUSPmRNA_se,lw=1,
    markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(exp.t5/60.,exp.hrg_DUSPmRNA_av,yerr=exp.hrg_DUSPmRNA_se,lw=1,
    markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.plot(t,DUSPmRNA[:,0]/np.max(DUSPmRNA[:,1]),'b')
plt.plot(t,DUSPmRNA[:,1]/np.max(DUSPmRNA[:,1]),'r')
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel(r'$\it{dusp}$'+' mRNA\nexpression')

plt.subplot(2,4,6)
e = plt.errorbar(exp.t4/60.,exp.egf_cFosmRNA_av,yerr=exp.egf_cFosmRNA_se,lw=1,
    markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(exp.t4/60.,exp.hrg_cFosmRNA_av,yerr=exp.hrg_cFosmRNA_se,lw=1,
    markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.plot(t,cFosmRNA[:,0]/np.max(cFosmRNA[:,1]),'b')
plt.plot(t,cFosmRNA[:,1]/np.max(cFosmRNA[:,1]),'r')
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel(r'$\it{c}$'+'-'+r'$\it{fos}$'+' mRNA\nexpression')

plt.subplot(2,4,7)
e = plt.errorbar(exp.t5/60.,exp.egf_cFosPro_av,yerr=exp.egf_cFosPro_se,lw=1,
    markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(exp.t5/60.,exp.hrg_cFosPro_av,yerr=exp.hrg_cFosPro_se,lw=1,
    markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.plot(t,cFosPro[:,0]/np.max(cFosPro[:,1]),'b')
plt.plot(t,cFosPro[:,1]/np.max(cFosPro[:,1]),'r')
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel('c-Fos Protein\nexpression')

plt.subplot(2,4,8)
e = plt.errorbar(exp.t2/60.,exp.egf_PcFos_av,yerr=exp.egf_PcFos_se,lw=1,
    markerfacecolor='None',markeredgecolor='b',fmt='bD',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
e = plt.errorbar(exp.t2/60.,exp.hrg_PcFos_av,yerr=exp.hrg_PcFos_se,lw=1,
    markerfacecolor='None',markeredgecolor='r',fmt='rs',capsize=8,clip_on=False)
for b in e[1]:
    b.set_clip_on(False)
plt.plot(t,PcFos[:,0]/np.max(PcFos[:,1]),'b')
plt.plot(t,PcFos[:,1]/np.max(PcFos[:,1]),'r')
plt.xlim(0,90)
plt.xticks([0,30,60,90])
plt.yticks([0,0.2,0.4,0.6,0.8,1,1.2])
plt.ylim(0,1.2)
plt.xlabel('Time (min)')
plt.ylabel('Phosphorylated c-Fos\nProtein expression')