--******************************************************************
--                                          Add indices for speed
--******************************************************************

CREATE INDEX IF NOT EXISTS Dem_empi_idx ON Dem (EMPI);
CREATE INDEX IF NOT EXISTS Dia_empi_idx ON Dia (EMPI);
CREATE INDEX IF NOT EXISTS Dia_code_idx ON Dia (Code);
CREATE INDEX IF NOT EXISTS Rdt_empi_idx ON Rdt (EMPI);
CREATE INDEX IF NOT EXISTS Rdt_accn_idx ON Rdt (Accession_Number);
CREATE INDEX IF NOT EXISTS Rad_empi_idx ON Rad (EMPI);
CREATE INDEX IF NOT EXISTS Rad_repn_idx ON Rad (Report_Number);
--add more ass needed...



--******************************************************************
--                      Find set of exclusionary diagnoses for this cohort
--******************************************************************

CREATE TABLE Xdia_ICD9_Codes AS
SELECT
	DISTINCT Code
FROM
	Dia
WHERE
	code BETWEEN '191' AND '191.999'				--Malignant neoplasm of brain
	OR code BETWEEN '225' AND '225.299'		--Benign neoplasm of brain, cranial nerves, cerebral meninges
	OR code BETWEEN '237.1' AND '237.199'		--Neoplasm of uncertain behavior of pineal gland +/-
	OR code BETWEEN '237.5' AND '237.599'		--Neoplasm of uncertain behavior of brain and spinal cord
	OR code BETWEEN '237.6' AND '237.699'		--Neoplasm of uncertain behavior of meninges
	OR code BETWEEN '237.7' AND '237.799'		--Neurofibromatosis
	OR code BETWEEN '242' AND '242.999'		--Thyrotoxicosis with or without goiter
	OR code BETWEEN '260' AND '260.999'		--Kwashiorkor
	OR code BETWEEN '261' AND '261.999'		--Nutritional marasmus
	OR code BETWEEN '262' AND '262.999'		--Other severe protein-calorie malnutrition
	OR code BETWEEN '263' AND '263.999'		--Other and unspecified protein-calorie malnutrition
	OR code BETWEEN '269' AND '269.999'		--Other nutritional deficiencies
	OR code BETWEEN '270' AND '270.999'		--Disorders of amino-acid transport and metabolism
	OR code BETWEEN '271' AND '271.999'		--Disorders of carbohydrate transport and metabolism
	OR code BETWEEN '272' AND '272.999'		--Disorders of lipoid metabolism
	OR code BETWEEN '273' AND '273.999'		--Disorders of plasma protein metabolism
	OR code BETWEEN '275' AND '275.999'		--Disorders of mineral metabolism
	OR code BETWEEN '276' AND '276.999'		--Disorders of fluid electrolyte and acid-base balance
	OR code BETWEEN '277' AND '277.999'		--Other and unspecified disorders of metabolism
	OR code BETWEEN '278' AND '278.999'		--Overweight, obesity and other hyperalimentation 
	OR code BETWEEN '279' AND '279.999'		--Disorders involving the immune mechanism
	OR code BETWEEN '290' AND '290.999'		--Dementias
	OR code BETWEEN '291' AND '291.999'		--Alcohol-induced mental disorders
	OR code BETWEEN '292' AND '292.999'		--Drug-induced mental disorders
	OR code BETWEEN '294' AND '294.999'		--Persistent mental disorders due to conditions classified elsewhere
	OR code BETWEEN '297' AND '297.999'		--Delusional disorders
	OR code BETWEEN '299' AND '299.999'		--Pervasive developmental disorders
	OR code BETWEEN '300' AND '300.999'		--Anxiety, dissociative and somatoform disorders
	OR code BETWEEN '303' AND '303.999'		--Alcohol dependence syndrome 
	OR code BETWEEN '304' AND '304.999'		--Drug dependence
	OR code BETWEEN '305' AND '305.999'		--Nondependent abuse of drugs
	OR code BETWEEN '307' AND '307.099'		--Adult onset fluency disorder
	OR code BETWEEN '307.1' AND '307.199'		--Anorexia nervosa
	OR code BETWEEN '307.2' AND '307.299'		--Tics
	OR code BETWEEN '307.3' AND '307.399'		--Stereotypic movement disorder
	OR code BETWEEN '307.5' AND '307.599'		--Other and unspecified disorders of eating
	OR code BETWEEN '310' AND '310.999'   		--Specific nonpsychotic mental disorders due to brain damage
	OR code BETWEEN '314' AND '314.999'   		--Hyperkinetic syndrome of childhood
	OR code BETWEEN '315' AND '315.999'   		--Specific delays in development
	OR code BETWEEN '317' AND '317.999'   		--Mild intellectual disabilities
	OR code BETWEEN '318' AND '318.999'   		--Other specified intellectual disabilities
	OR code BETWEEN '319' AND '319.999'   		--Unspecified intellectual disabilities
	OR code BETWEEN '320' AND '320.999'   		--Bacterial meningitis
	OR code BETWEEN '321' AND '321.999'   		--Meningitis due to other organisms
	OR code BETWEEN '322' AND '322.999'   		--Meningitis of unspecified cause
	OR code BETWEEN '323' AND '323.999'   		--Encephalitis myelitis and encephalomyelitis
	OR code BETWEEN '324' AND '324.099'   		--Intracranial abscess
	OR code BETWEEN '325' AND '325.999'   		--Phlebitis and thrombophlebitis of intracranial venous sinuses
	OR code BETWEEN '326' AND '326.999'   		--Late effects of intracranial abscess or pyogenic infection
	OR code BETWEEN '327' AND '327.999'   		--* Organic sleep disorders *
	OR code BETWEEN '330' AND '330.999'   		--Cerebral degenerations usually manifest in childhood
	OR code BETWEEN '331' AND '331.999'   		--Other cerebral degenerations
	OR code BETWEEN '332' AND '332.999'   		--Parkinson's disease
	OR code BETWEEN '333' AND '333.999'   		--Other extrapyramidal disease and abnormal movement disorders
	OR code BETWEEN '334' AND '334.999'   		--Spinocerebellar disease
	OR code BETWEEN '335' AND '335.999'   		--Anterior horn cell disease
	OR code BETWEEN '336' AND '336.999'   		--Other diseases of spinal cord
	OR code BETWEEN '337' AND '337.999'   		--Disorders of the autonomic nervous system
	OR code BETWEEN '340' AND '340.999'   		--Multiple sclerosis
	OR code BETWEEN '341' AND '341.999'   		--Other demyelinating diseases of central nervous system
	OR code BETWEEN '342' AND '342.999'   		--Hemiplegia and hemiparesis
	OR code BETWEEN '343' AND '343.999'   		--Infantile cerebral palsy
	OR code BETWEEN '344' AND '344.999'   		--Other paralytic syndromes
	OR code BETWEEN '345' AND '345.999'   		--Epilepsy and recurrent seizures
	OR code BETWEEN '348' AND '348.999'   		--Other conditions of brain ??
	OR code BETWEEN '349.1' AND '349.199' 	--Nervous system complications from surgically implanted device
	OR code BETWEEN '349.8' AND '349.899' 	--Other specified disorders of nervous system
	OR code BETWEEN '358' AND '358.999'		--Myoneural disorders
	OR code BETWEEN '359' AND '359.999'		--Muscular dystrophies and other myopathies
	OR code BETWEEN '369' AND '369.999'		--Blindness and low vision
	OR code BETWEEN '430' AND '430.999'		--Subarachnoid hemorrhage
	OR code BETWEEN '431' AND '431.999'		--Intracerebral hemorrhage
	OR code BETWEEN '432' AND '432.999'		--Other and unspecified intracranial hemorrhage
	OR code BETWEEN '433' AND '433.999'		--Occlusion and stenosis of precerebral arteries
	OR code BETWEEN '434' AND '434.999'		--Occlusion of cerebral arteries
	OR code BETWEEN '435' AND '435.999'		--Transient cerebral ischemia
	OR code BETWEEN '438' AND '438.999'		--Late effects of cerebrovascular disease
	OR code BETWEEN '742' AND '742.999'		--Other congenital anomalies of nervous system
	OR code BETWEEN '758' AND '758.999'		--Chromosomal anomalies
	OR code BETWEEN '764' AND '764.999'		--Slow fetal growth and fetal malnutrition
	OR code BETWEEN '765' AND '765.999'		--Disorders relating to short gestation and low birthweight
	OR code BETWEEN '766' AND '766.999'		--Disorders relating to long gestation and high birthweight
	OR code BETWEEN '767' AND '767.099'		--Subdural and cerebral hemorrhage
	OR code BETWEEN '767.4' AND '767.499'		--Injury to spine and spinal cord due to birth trauma
	OR code BETWEEN '767.5' AND '767.599'		--Facial nerve injury due to birth trauma
	OR code BETWEEN '767.7' AND '767.799'		--Other cranial and peripheral nerve injuries due to birth trauma
	OR code BETWEEN '772' AND '772.999'   		--Fetal and neonatal hemorrhage
	OR code BETWEEN '773' AND '773.999'   		--Hemolytic disease of fetus or newborn due to isoimmunization
	OR code BETWEEN '775' AND '775.999'   		--Endocrine and metabolic disturbances specific to the fetus and newborn

	-- Strict excluding diagnoses
	--OR code BETWEEN '192' AND '192.999'		--* Malignant neoplasm of other and unspecified parts of nervous system *
	--OR code BETWEEN '237' AND '237.099'		--* Neoplasm of uncertain behavior of pituitary gland and craniopharyngeal duct *
	--OR code BETWEEN '237.9' AND '237.999'		--* Neoplasm of uncertain behavior of other and unspecified parts of nervous system *
	--OR code BETWEEN '240' AND '240.999'		--* Simple and unspecified goiter *
	--OR code BETWEEN '241' AND '241.999'		--* Nontoxic nodular goiter *
	--OR code BETWEEN '243' AND '243.999'		--* Congenital hypothyroidism *
	--OR code BETWEEN '244' AND '244.999'		--* Acquired hypothyroidism *
	--OR code BETWEEN '245' AND '245.999'		--* Thyroiditis *
	--OR code BETWEEN '246' AND '246.999'		--* Other disorders of thyroid *
	--OR code BETWEEN '264' AND '264.999'		--* Vitamin a deficiency *
	--OR code BETWEEN '265' AND '265.999'		--* Thiamine and niacin deficiency states *
	--OR code BETWEEN '266' AND '266.999'		--* Deficiency of b-complex components  *
	--OR code BETWEEN '267' AND '267.999'		--* Ascorbic acid deficiency *
	--OR code BETWEEN '268' AND '268.999'		--* Vitamin d deficiency *
	--OR code BETWEEN '274' AND '274.999'		--* Gout *
	--OR code BETWEEN '295' AND '295.999'		--* Schizophrenic disorders *
	--OR code BETWEEN '296' AND '296.999'		--* Episodic mood disorders *
	--OR code BETWEEN '298' AND '298.999'		--* Other nonorganic psychoses *
	--OR code BETWEEN '301' AND '301.999'		--* Personality disorders *
	--OR code BETWEEN '302' AND '302.999'		--* Sexual and gender identity disorders *
	--OR code BETWEEN '776' AND '776.999'		--* Hematological disorders of newborn *
	--OR code BETWEEN '777' AND '777.999'		--* Perinatal disorders of digestive system *

ORDER BY
	Code
;
CREATE INDEX IF NOT EXISTS Xdia_code_idx ON Xdia_ICD9_Codes (Code);



-- ------------------------------------------------------------------------------------------------------------------
-- Get breakdown of patients with exclusion diagnoses
CREATE TABLE Xdia_patient_breakdown AS
SELECT
	Code,
	Diagnosis_Name,
	count(DISTINCT EMPI) AS Patient_N
FROM
	Dia
WHERE
	Code IN Xdia_ICD9_Codes
GROUP BY
	Code
ORDER BY
	Patient_N DESC
;




--*****************************************************************************
--                                                   Compute Features
--*****************************************************************************


-- create Features table
CREATE TABLE IF NOT EXISTS Features AS SELECT DISTINCT EMPI FROM Con;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "Rad_count"
CREATE TABLE Features_New AS
SELECT 
	Features.*, --old columns
	CASE WHEN RadCount > 0 THEN RadCount ELSE 0 END AS Rad_count --new column; ensure NOT NULL
FROM 
	Features 
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, number of Rad events] table
	SELECT
		EMPI AS xEMPI, 
		count(*) AS RadCount 
	FROM 
		Rad 
	GROUP BY EMPI
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "Rdt_count"
CREATE TABLE Features_New AS
SELECT 
	Features.*, --old columns
	CASE WHEN RdtCount > 0 THEN RdtCount ELSE 0 END AS Rdt_count --new column; ensure NOT NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, number of Rdt events] table
	SELECT
		EMPI AS xEMPI, 
		count(*) AS RdtCount 
	FROM 
		Rdt
	GROUP BY EMPI
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- **** no ICD-10 codes in this dataset ****

-- add column "Dia_count"
CREATE TABLE Features_New AS
SELECT 
	Features.*, --old columns
	CASE WHEN DiaCount > 0 THEN DiaCount ELSE 0 END AS Dia_count --old column; ensure NOT NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, number of Dia events] table
	SELECT
		EMPI AS xEMPI, 
		count(*) AS DiaCount 
	FROM 
		Dia
	GROUP BY EMPI
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "Max_xdia_count"
CREATE TABLE Features_New AS
SELECT
	Features.*, --old columns
	CASE WHEN MaxXdiaCount > 0 THEN MaxXdiaCount ELSE 0 END AS Max_xdia_count --new column; ensure NOT NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, maximum of counts of exlusion diagnoses] table;
	-- includes only exclusion diagnoses, and patients who have them
	SELECT DISTINCT
		EMPI AS xEMPI,
		max(XdiaCount) AS MaxXdiaCount
	FROM
		(
		-- [EMPI, ICD-9 code, number of this ICD-9-code events] table;
		-- includes only exclusion diagnoses, and patients who have them
		SELECT
			EMPI,
			Code,
			count(Code) AS XdiaCount
		FROM 
			Dia 
		WHERE
			Code IN Xdia_ICD9_Codes
		GROUP BY 
			Code, EMPI
		ORDER BY
			EMPI
		)
	GROUP BY 
		EMPI
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "Rdt_brain_mri_count"
CREATE TABLE Features_New AS
SELECT
	Features.*, --old columns
	CASE WHEN RdtBrainMriCount > 0 THEN RdtBrainMriCount ELSE 0 END AS Rdt_brain_mri_count --new column; ensure NOT NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, has a brain MRI boolean] table; only patients with this Rdt event
	SELECT DISTINCT
		EMPI AS xEMPI,
		count(*) AS RdtBrainMriCount
	FROM
		Rdt
	WHERE --patient has brain MRI
		Rdt.'Mode' LIKE 'MRI%' -- e.g. 'MRI', 'MRI.ANGIO'
		AND Rdt.'Group'='HDNK' -- head/neck
		AND (
			-- only whole head and brain tests
			Rdt.'Test_Description' LIKE '%brain%'
			OR Rdt.'Test_Description' LIKE '%head%'
		)
	GROUP BY 
		EMPI
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "First_Rdt_brain_mri"
CREATE TABLE Features_New AS
SELECT
	Features.*, --old columns
	FirstRdtBrainMri AS First_Rdt_brain_mri --new column; is Date; can be NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, date of earliest brain MRI] table; only patients with this Rdt event
	SELECT
		EMPI AS xEMPI,
		min(Rdt.Date) AS FirstRdtBrainMri
	FROM
		Rdt
	WHERE --patient has brain MRI
		Rdt.'Mode' LIKE 'MRI%' -- e.g. 'MRI', 'MRI.ANGIO'
		AND Rdt.'Group'='HDNK' -- head/neck
		AND (
			-- only whole head and brain tests
			Rdt.'Test_Description' LIKE '%brain%'
			OR Rdt.'Test_Description' LIKE '%head%'
		)
	GROUP BY
		EMPI
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "Last_Rdt_brain_mri"
CREATE TABLE Features_New AS
SELECT
	Features.*, --old columns
	LastRdtBrainMri AS Last_Rdt_brain_mri --new column; is Date; can be NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, date of latest brain MRI] table; only patients with this Rdt event
	SELECT
		EMPI AS xEMPI,
		max(Rdt.Date) AS LastRdtBrainMri
	FROM
		Rdt
	WHERE --patient has brain MRI
		Rdt.'Mode' LIKE 'MRI%' -- e.g. 'MRI', 'MRI.ANGIO'
		AND Rdt.'Group'='HDNK' -- head/neck
		AND (
			-- only whole head and brain tests
			Rdt.'Test_Description' LIKE '%brain%'
			OR Rdt.'Test_Description' LIKE '%head%'
		)
	GROUP BY
		EMPI
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "Age_at_first_Rdt_brain_mri"
CREATE TABLE Features_New AS
SELECT
	Features.*, --old columns
	AgeAtFirstRdtBrainMri AS Age_at_first_Rdt_brain_mri --new column; is Integer; can be NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, age in years at the first brain MRI] table; only patients with this Rdt event
	SELECT
		EMPI AS xEMPI,
		round( ( ( julianday( FirstRdtBrainMri) - julianday(Dem.'Date_of_Birth') ) / 365 ), 2 ) AS AgeAtFirstRdtBrainMri --age in years rounded to 2 decimal points
	FROM
		(
		-- [EMPI, date of earliest brain MRI] table; only patients with this Rdt event
		SELECT
			EMPI AS yEMPI,
			min(Rdt.Date) AS FirstRdtBrainMri
		FROM
			Rdt
		WHERE --patient has brain MRI
			Rdt.'Mode' LIKE 'MRI%' -- e.g. 'MRI', 'MRI.ANGIO'
			AND Rdt.'Group'='HDNK' -- head/neck
			AND (
				-- only whole head and brain tests
				Rdt.'Test_Description' LIKE '%brain%'
				OR Rdt.'Test_Description' LIKE '%head%'
			)
		GROUP BY
			EMPI
		)
	LEFT JOIN
		Dem
	ON
		yEMPI = Dem.'EMPI'
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "Age_at_last_Rdt_brain_mri"
CREATE TABLE Features_New AS
SELECT
	Features.*, --old columns
	AgeAtLastRdtBrainMri AS Age_at_last_Rdt_brain_mri --new column; is Integer; can be NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, age in years at the last brain MRI] table; only patients with this Rdt event
	SELECT
		EMPI AS xEMPI,
		round( ( ( julianday( FirstRdtBrainMri) - julianday(Dem.'Date_of_Birth') ) / 365 ), 2 ) AS AgeAtLastRdtBrainMri --age in years rounded to 2 decimal points
	FROM
		(
		-- [EMPI, date of latest brain MRI] table; only patients with this Rdt event
		SELECT
			EMPI AS yEMPI,
			max(Rdt.Date) AS FirstRdtBrainMri
		FROM
			Rdt
		WHERE --patient has brain MRI
			Rdt.'Mode' LIKE 'MRI%' -- e.g. 'MRI', 'MRI.ANGIO'
			AND Rdt.'Group'='HDNK' -- head/neck
			AND (
				-- only whole head and brain tests
				Rdt.'Test_Description' LIKE '%brain%'
				OR Rdt.'Test_Description' LIKE '%head%'
			)
		GROUP BY
			EMPI
		)
	LEFT JOIN
		Dem
	ON
		yEMPI = Dem.'EMPI'
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "Rad_brain_mri_count"
CREATE TABLE Features_New AS
SELECT
	Features.*, --old columns
	CASE WHEN RadBrainMriCount > 0 THEN RadBrainMriCount ELSE 0 END AS Rad_brain_mri_count --new column; ensure NOT NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, has a brain MRI boolean] table; only patients with this Rad event
	SELECT DISTINCT
		EMPI AS xEMPI,
		count(*) AS RadBrainMriCount
	FROM
		Rad
	WHERE --patient has brain MRI
		Report_Description like '%MR%Head%'
	OR
		Report_Description like '%MR%Brain%'
	GROUP BY 
		EMPI
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "First_Rad_brain_mri"
CREATE TABLE Features_New AS
SELECT
	Features.*, --old columns
	FirstRadBrainMri AS First_Rad_brain_mri --new column; is Date; can be NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, date of earliest brain MRI] table; only patients with this Rad event
	SELECT
		EMPI AS xEMPI,
		min(Rad.Report_Date_Time) AS FirstRadBrainMri
	FROM
		Rad
	WHERE --patient has brain MRI
		Report_Description like '%MR%Head%'
	OR
		Report_Description like '%MR%Brain%'
	GROUP BY
		EMPI
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "Last_Rad_brain_mri"
CREATE TABLE Features_New AS
SELECT
	Features.*, --old columns
	LastRadBrainMri AS Last_Rad_brain_mri --new column; is Date; can be NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, date of latest brain MRI] table; only patients with this Rad event
	SELECT
		EMPI AS xEMPI,
		max(Rad.Report_Date_Time) AS LastRadBrainMri
	FROM
		Rad
	WHERE --patient has brain MRI
		Report_Description like '%MR%Head%'
	OR
		Report_Description like '%MR%Brain%'
	GROUP BY
		EMPI
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "Age_at_first_Rad_brain_mri"
CREATE TABLE Features_New AS
SELECT
	Features.*, --old columns
	AgeAtFirstRadBrainMri AS Age_at_first_Rad_brain_mri --new column; is Integer; can be NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, age in years at the earliest brain MRI] table; only patients with this Rad event
	SELECT
		EMPI AS xEMPI,
		round( ( ( julianday( FirstRadBrainMri) - julianday(Dem.'Date_of_Birth') ) / 365 ), 2 ) AS AgeAtFirstRadBrainMri --age in years rounded to 2 decimal points
	FROM
		(
		-- [EMPI, date of earliest brain MRI] table; only patients with this Rad event
		SELECT
			EMPI AS yEMPI,
			min(Rad.Report_Date_Time) AS FirstRadBrainMri
		FROM
			Rad
		WHERE --patient has brain MRI
			Report_Description like '%MR%Head%'
		OR
			Report_Description like '%MR%Brain%'
		GROUP BY
			EMPI
		)
	LEFT JOIN
		Dem
	ON
		yEMPI = Dem.EMPI
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "Age_at_last_Rad_brain_mri"
CREATE TABLE Features_New AS
SELECT
	Features.*, --old columns
	AgeAtLastRadBrainMri AS Age_at_last_Rad_brain_mri --new column; is Integer; can be NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, age in years at the last brain MRI] table; only patients with this Rad event
	SELECT
		EMPI AS xEMPI,
		round( ( ( julianday( LastRadBrainMri) - julianday(Dem.'Date_of_Birth') ) / 365 ), 2 ) AS AgeAtLastRadBrainMri --age in years rounded to 2 decimal points
	FROM
		(
		-- [EMPI, date of latest brain MRI] table; only patients with this Rad event
		SELECT
			EMPI AS yEMPI,
			max(Rad.Report_Date_Time) AS LastRadBrainMri
		FROM
			Rad
		WHERE --patient has brain MRI
			Report_Description like '%MR%Head%'
		OR
			Report_Description like '%MR%Brain%'
		GROUP BY
			EMPI
		)
	LEFT JOIN
		Dem
	ON
		yEMPI = Dem.EMPI
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;



-- ------------------------------------------------------------------------------------------------------------------
-- add column "Has_normative_phrase_in_Rad"
CREATE TABLE Features_New AS
SELECT
	Features.*, --old columns
	CASE WHEN HasNormativePhraseInRad > 0 THEN 1 ELSE 0 END AS Has_normative_phrase_in_Rad --new column; ensure NOT NULL
FROM 
	Features
LEFT JOIN --ensure same rows as old features table
	(
	-- [EMPI, has-a-normative-phrase-in-the-Rad-report boolean] table; only patients with this Rad event
	SELECT DISTINCT
		EMPI AS xEMPI,
		1 AS HasNormativePhraseInRad
	FROM
		Rad
	WHERE --report contains a normitive phrase
		     Report_Text LIKE '% Age-appropriate MRI of the brain with no structural abnormality identified%'
		OR Report_Text LIKE '% MRI appearance of the brain is age appropriate%'
		OR Report_Text LIKE '% MRI of the brain normal for corrected gestational age without evidence of prior injury%'
		OR Report_Text LIKE '% Negative exam%'
		OR Report_Text LIKE '% No abnormality is seen on this unenhanced MRI of the brain%'
		OR Report_Text LIKE '% No acute abnormality identified%'
		OR Report_Text LIKE '% No definite structural abnormality identified%'
		OR Report_Text LIKE '% No evidence of acute intracranial abnormality%'
		OR Report_Text LIKE '% No evidence of diffusion weighted or gross FLAIR abnormalities%'
		OR Report_Text LIKE '% No evidence of focal mass lesion or cortical abnormality%'
		OR Report_Text LIKE '% No evidence of intracranial pathology%'
		OR Report_Text LIKE '% No evidence of morphological abnormality. Unremarkable Brain MRI%'
		OR Report_Text LIKE '% No evidence of structural abnormality, infarction or hemorrhage%'
		OR Report_Text LIKE '% No intracranial abnormality identified%'
		OR Report_Text LIKE '% No intracranial structural abnormality by MRI%'
		OR Report_Text LIKE '% No significant abnormality seen%'
		OR Report_Text LIKE '% No structural abnormality identified%'
		OR Report_Text LIKE '% Normal age-appropriate MRI of the brain%'
		OR Report_Text LIKE '% Normal brain MRI%'
		OR Report_Text LIKE '% Normal brain MRI for age%'
		OR Report_Text LIKE '% Normal brain MRI without evidence of structural anomaly or other CNS abnormality%'
		OR Report_Text LIKE '% Normal brain%'
		OR Report_Text LIKE '% Normal contrast enhanced MRI of the brain%'
		OR Report_Text LIKE '% Normal conventional MR appearance of the brain%'
		OR Report_Text LIKE '% NORMAL EXAMINATION%'
		OR Report_Text LIKE '% Normal findings%'
		OR Report_Text LIKE "% Normal MR appearance of the brain for the patient's age%"
		OR Report_Text LIKE '% Normal MR evaluation of the brain%'
		OR Report_Text LIKE '% Normal MRI of the brain%'
		OR Report_Text LIKE '% Normal MRI of the brain for age without evidence of structural abnormality%'
		OR Report_Text LIKE '% Normal MRI of the brain parenchyma%'
		OR Report_Text LIKE '% Normal MRI study of the brain%'
		OR Report_Text LIKE '% Normal myelination by MR imaging%'
		OR Report_Text LIKE '% Normal non-contrast MRI of the brain%'
		OR Report_Text LIKE '% Normal nonenhanced MRI of the brain for age%'
		OR Report_Text LIKE '% Normal pediatric brain MRI and MRV, with no acute pathology identified to account for the seizure%'
		OR Report_Text LIKE '% NORMAL PEDIATRIC BRAIN MRI WITH NO PATHOLOGY IDENTIFIED%'
		OR Report_Text LIKE '% Normal study%'
		OR Report_Text LIKE '% NORMAL STUDY FOR AGE%'
		OR Report_Text LIKE '% Normal unenhanced MRI of the brain%'
		OR Report_Text LIKE '% The brain appears normal. There is no evidence of a cortical dysplasia%'
		OR Report_Text LIKE '% The brain is normal for age%'
		OR Report_Text LIKE '% Unremarkable age appropriate MRI brain%'
		OR Report_Text LIKE '% Unremarkable brain MRI%'
		OR Report_Text LIKE '% Unremarkable MR appearance of the brain. No brainstem or cranial nerve abnormality identified%'
		OR Report_Text LIKE '% Unremarkable MRI brain. Myelination within normal limits of normal for age%'
		OR Report_Text LIKE '% Unremarkable MRI of the brain%'
		OR Report_Text LIKE '% Unremarkable MRI of the brain with no evidence of intracranial mass or acute territorial infarction%'
		OR Report_Text LIKE '% Unremarkable nonenhanced MRI of the brain%'
		OR Report_Text LIKE '% UNREMARKABLE STUDY%'
	) 
ON
	Features.EMPI = xEMPI
;
DROP TABLE Features;
ALTER TABLE Features_New RENAME TO Features;




--******************************************************************
--                               Search Features for Potential cohort
--******************************************************************

CREATE TABLE Features_potential_cohort AS
SELECT
	*
FROM 
	Features																										--n=?
WHERE
	(Rad_count > 0 OR Rdt_count	> 0)																	--n=?
AND
	(Last_Rdt_brain_mri >= '2000-01-01' OR Last_Rad_brain_mri >= '2000-01-01')	--n=?
AND
	(Age_at_first_Rdt_brain_mri <= 6.0 OR Age_at_first_Rad_brain_mri <= 6.0)		--n=?
AND
	(Max_xdia_count < 2) 																					--n=?
;








