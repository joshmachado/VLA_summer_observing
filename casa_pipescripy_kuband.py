__rethrow_casa_exceptions = True
context = h_init()
context.set_state('ProjectSummary', 'observatory', 'Karl G. Jansky Very Large Array')
context.set_state('ProjectSummary', 'telescope', 'EVLA')
try:
 hifv_importdata(vis=['TDEM0009_Kuband.ms'],createmms='automatic', asis='Receiver CalAtmosphere', ocorr_mode='co',nocopy=False, overwrite=False)
 #hifv_hanning(pipelinemode="automatic")
 hifv_flagdata(tbuff=0.0, flagbackup=False, scan=True, fracspw=0.05,intents='*POINTING*,*FOCUS*,*ATMOSPHERE*,*SIDEBAND_RATIO*, *UNKNOWN*,*SYSTEM_CONFIGURATION*, *UNSPECIFIED#UNSPECIFIED*', clip=True, baseband=True,shadow=True, quack=True, edgespw=True, autocorr=True, hm_tbuff='1.5int',template=True, online=True)
 hifv_vlasetjy(fluxdensity=-1, scalebychan=True, spix=0, reffreq='1GHz')
 hifv_priorcals(tecmaps=False)
 hifv_testBPdcals(weakbp=False)
 #hifv_flagbaddef(doflagundernspwlimit=True)
 hifv_checkflag(pipelinemode="automatic")
 hifv_semiFinalBPdcals(weakbp=False)
 hifv_checkflag(checkflagmode='semi')
 hifv_semiFinalBPdcals(weakbp=False)
 hifv_solint(pipelinemode="automatic")
 hifv_fluxboot(pipelinemode="automatic")
 hifv_finalcals(weakbp=False)
 hifv_applycals(flagdetailedsum=True, gainmap=False, flagbackup=True, flagsum=True)
 hifv_targetflag(intents='*CALIBRATE*')
 hifv_statwt(pipelinemode="automatic")
 hifv_plotsummary(pipelinemode="automatic")
 hif_makeimlist(nchan=-1, calcsb=False, intent='PHASE,BANDPASS', robust=-999.0,per_eb=False, calmaxpix=300, specmode='cont', clearlist=True)
 hif_makeimages(tlimit=2.0, hm_minbeamfrac=-999.0, hm_dogrowprune=True,hm_negativethreshold=-999.0, calcsb=False, target_list={},hm_noisethreshold=-999.0, hm_masking='none', hm_minpercentchange=-999.0,parallel='automatic', masklimit=4, hm_lownoisethreshold=-999.0,hm_growiterations=-999, cleancontranges=False, hm_sidelobethreshold=-999.0)
finally:
 h_save()
