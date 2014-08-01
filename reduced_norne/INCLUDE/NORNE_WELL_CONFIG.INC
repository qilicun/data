--------------------------------------------
--=======Production Wells========--
-------------------------------------------- 

--
--INCLUDE
-- './INCLUDE/VFP/DevNew.VFP' / 

--
--INCLUDE
-- './INCLUDE/VFP/E1h.VFP' / 
--
--INCLUDE
-- './INCLUDE/VFP/NEW_D2_GAS_0.00003.VFP' / 
--
--INCLUDE
-- './INCLUDE/VFP/GAS_PD2.VFP' / 
--
--INCLUDE
-- './INCLUDE/VFP/AlmostVertNew.VFP' / 
--
--INCLUDE
-- './INCLUDE/VFP/GasProd.VFP' / 
  
 
-- 01.01.07 new VFP curves for producing wells, matched with the latest well tests in Prosper. lmarr

--
--INCLUDE
-- './INCLUDE/VFP/B1BH.Ecl' / 
--
--INCLUDE
-- './INCLUDE/VFP/B2H.Ecl' / 
--
--INCLUDE
-- './INCLUDE/VFP/B3H.Ecl' / 
--
--INCLUDE
-- './INCLUDE/VFP/B4DH.Ecl' / 
--
--INCLUDE
-- './INCLUDE/VFP/D1CH.Ecl' / 
--
--INCLUDE
-- './INCLUDE/VFP/D2H.Ecl' / 
--
---INCLUDE
-- './INCLUDE/VFP/D3BH.Ecl' / 
--
--INCLUDE
-- './INCLUDE/VFP/E1H.Ecl' / 
--
--INCLUDE
-- './INCLUDE/VFP/E3CH.Ecl' / 
--
--INCLUDE
-- './INCLUDE/VFP/K3H.Ecl' / 
 
--------------------------------------------
--=======Production Flowlines========--
-------------------------------------------- 
--
-- 16.5.02 new VFP curves for southgoing PD1,PD2,PB1,PB2 flowlines -> pd2.VFP
--
--INCLUDE
-- './INCLUDE/VFP/pd2.VFP' / 
--
-- 16.5.02 new VFP curves for northgoing PE1,PE2 flowlines -> pe2.VFP
--
--INCLUDE
-- './INCLUDE/VFP/pe2.VFP' / 
 
  
-- 24.11.06 new matched VLP curves for PB1 valid from 01.07.06
--
--INCLUDE
-- './INCLUDE/VFP/PB1.PIPE.Ecl' / 

--24.11.06 new matched VLP curves for PB2 valid from 01.07.06
--
--INCLUDE
-- './INCLUDE/VFP/PB2.PIPE.Ecl' / 

--24.11.06 new matched VLP curves for PD1 valid from 01.07.06
--
--INCLUDE
-- './INCLUDE/VFP/PD1.PIPE.Ecl' / 

--24.11.06 new matched VLP curves for PD2 valid from 01.07.06
--
--INCLUDE
-- './INCLUDE/VFP/PD2.PIPE.Ecl' / 

--24.11.06 new matched VLP curves for PE1 valid from 01.07.06
--
--INCLUDE
-- './INCLUDE/VFP/PE1.PIPE.Ecl' / 

--24.11.06 new matched VLP curves for PE2 valid from 01.07.06
--
--INCLUDE
-- './INCLUDE/VFP/PE2.PIPE.Ecl' / 
  
   
-------------------------------------------
--=======INJECTION FLOWLINES 08.09.2005     ========--
--------------------------------------------
-- VFPINJ nr. 10 Water injection flowline WIC 
--
--INCLUDE
-- './INCLUDE/VFP/WIC.PIPE.Ecl' / 

-- VFPINJ nr. 11 Water injection flowline WIF 
--
--INCLUDE
-- './INCLUDE/VFP/WIF.PIPE.Ecl' / 

--------------------------------------------
--=======   INJECTION Wells 08.09.2005       ========--
--------------------------------------------
-- VFPINJ nr. 12 Water injection wellbore Norne C-1H 
--
--INCLUDE
-- './INCLUDE/VFP/C1H.Ecl' / 

-- VFPINJ nr. 13 Water injection wellbore Norne C-2H 
--
--INCLUDE
-- './INCLUDE/VFP/C2H.Ecl' / 

-- VFPINJ nr. 14 Water injection wellbore Norne C-3H 
--
--INCLUDE
-- './INCLUDE/VFP/C3H.Ecl' / 

-- VFPINJ nr. 15 Water injection wellbore Norne C-4H 
--
--INCLUDE
-- './INCLUDE/VFP/C4H.Ecl' / 

-- VFPINJ nr. 16 Water injection wellbore Norne C-4AH 
--
--INCLUDE
-- './INCLUDE/VFP/C4AH.Ecl' / 

-- VFPINJ nr. 17 Water injection wellbore Norne F-1H 
--
--INCLUDE
-- './INCLUDE/VFP/F1H.Ecl' / 

-- VFPINJ nr. 18 Water injection wellbore Norne F-2H 
--
--INCLUDE
-- './INCLUDE/VFP/F2H.Ecl' / 

-- VFPINJ nr. 19 Water injection wellbore Norne F-3 H
--
--INCLUDE
--'./INCLUDE/VFP/F3H.Ecl' / 

-- VFPINJ nr. 20 Water injection wellbore Norne F-4H 
--
--INCLUDE
--'./INCLUDE/VFP/F4H.Ecl' / 

TUNING
1 10  0.1  0.15  3  0.3  0.3  1.20  /
5*   0.1   0.0001   0.02  0.02  /
2* 40 1* 15 /
/

-- only possible for ECL 2006.2+ version
ZIPPY2
'SIM=4.2' 'MINSTEP=1E-6' /

-- PI reduction in case of water cut
INCLUDE
'./INCLUDE/PI/pimultab_low-high_aug-2006.inc' / 

-- History
INCLUDE
'./INCLUDE/BC0407_HIST01122006.SCH' / 

END
