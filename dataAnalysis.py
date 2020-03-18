
import pandas as pd
import numpy as np
import math
import re
from datetime import datetime


def run():

	# -- Completeness -- #

	filename = 'Sample Prediction Model Data_19022020.csv'
	df = pd.read_csv(filename)

	# -- Select relevant Data -- #

	clinical_data_df = df[['Sample ID', 'DOB', 'Date of Onset', 'Site of onset', 'El Escorial', 'Date of Diagnosis', 'Onset To Diagnosis(months)', 'Onset To Death(months)',
	'Diagnosis to Death(months)','Date of Death','Does the patient have dementia?','C9orf72 Repeat Expansion']];



	# -- Count missing cells -- #

	variableMetaData = pd.DataFrame();
	variableMetaData['Empty Cells'] = df.isnull().sum();
	variableMetaData['Completeness %'] = 100-(df.isnull().sum()/12*100);

	empty_cells_by_row = pd.DataFrame();
	empty_cells_by_row['Sample ID'] = df.iloc[:,0];
	empty_cells_by_row['Empty Cells'] = df.isnull().sum(axis=1);
	empty_cells_by_row['Completeness %'] = 100-(df.isnull().sum(axis=1)/len(df)*100);

	print('\n\nEmpty cells per patient:\n',empty_cells_by_row ,'\n\nEmpty cells by data category:\n',variableMetaData,'\n\n');


	# -- Timeliness -- #

	visit_df = pd.read_csv('clinical_visit_data.csv')
	visit_dates_df = visit_df[['Patient','Clinical visit date']]
	patient = None
	patient1 = None
	firstVisit = None
	lastVisit = None
	dateOfOnset = None
	dateOfDeath = None

	for ind in clinical_data_df.index:
		if(isinstance(clinical_data_df['Date of Onset'][ind], str) and isinstance(clinical_data_df['Date of Death'][ind], str)):
			dateOfDeath = datetime.strptime(clinical_data_df['Date of Onset'][ind], '%d/%m/%Y')
			dateOfOnset = datetime.strptime(clinical_data_df['Date of Death'][ind], '%d/%m/%Y')
			print('Days from diagnosis to death:', clinical_data_df['Sample ID'][ind], abs((dateOfDeath - dateOfOnset).days), "days")
		

	for ind in visit_dates_df.index:

		if ind==0 or (visit_dates_df['Patient'][ind]!=visit_dates_df['Patient'][ind-1]):
			firstVisit = datetime.strptime(visit_dates_df['Clinical visit date'][ind], '%d/%m/%Y')
			patient = visit_dates_df['Patient'][ind]


		if (ind==(len(visit_dates_df)-1) or (visit_dates_df['Patient'][ind]!=visit_dates_df['Patient'][ind+1])):
			lastVisit = datetime.strptime(visit_dates_df['Clinical visit date'][ind], '%d/%m/%Y')
			patient1 = visit_dates_df['Patient'][ind]

		if(firstVisit and lastVisit and (patient1 == patient)):
			print('Days from first clinical visit to last:', patient, abs((lastVisit - firstVisit).days), "days")


	# -- Accuracy -- #

	totalErrors = 0;
	siteOfOnsetErrors = 0;
	elEscorialErrors = 0;
	onsetToDiganosisErrors = 0;
	C9orf72Errors = 0;
	dementiaErrors = 0;
	DOBErrors = 0;

	for ind in clinical_data_df.index:

		# -- Site of onset -- #
		if ((clinical_data_df['Site of onset'][ind] == 'Spinal') or (clinical_data_df['Site of onset'][ind] == 'Bulbar') 
			or (clinical_data_df['Site of onset'][ind] == "Cognitive/Behavioural and Spinal") or (pd.isna(clinical_data_df['Site of onset'][ind]))):
			pass
		else:
			totalErrors+=1;
			siteOfOnsetErrors += 1;

	
		# -- El Escorial-- #
		if ((clinical_data_df['El Escorial'][ind] == 'Definite') or (clinical_data_df['El Escorial'][ind] == 'Probable') or (clinical_data_df['El Escorial'][ind] == "Possible") 
			or (clinical_data_df['El Escorial'][ind] == "Lab Supported Probable") or (pd.isna(clinical_data_df['El Escorial'][ind]))):
			pass
		else:
			totalErrors+=1;
			elEscorialErrors += 1;

	
		# -- Onset to Diagnosis -- #
		if (isinstance(clinical_data_df['Onset To Diagnosis(months)'][ind], float)):
			pass
		else:
			try: 
				float(clinical_data_df['Onset To Diagnosis(months)'][ind])
			except ValueError:
				totalErrors+=1;
				onsetToDiganosisErrors += 1;

	
		# -- C9orf72 Repeat Expansion -- #
		if ((clinical_data_df['C9orf72 Repeat Expansion'][ind] == bool(False)) or (clinical_data_df['C9orf72 Repeat Expansion'][ind] == bool(True)) or
		 (pd.isna(clinical_data_df['C9orf72 Repeat Expansion'][ind]))):
			pass
		else:
			totalErrors+=1;
			C9orf72Errors += 1;


		# -- Does the patient have dementia? -- #
		if ((clinical_data_df['Does the patient have dementia?'][ind] == bool(False)) or (clinical_data_df['Does the patient have dementia?'][ind] == bool(True)) or
		 (pd.isna(clinical_data_df['Does the patient have dementia?'][ind]))):
			pass
		else:
			totalErrors+=1;
			dementiaErrors +=1;

		# -- Date of Birth -- #
		r = re.compile('[0-3][0-9]/[0-1][0-9]/[1-2][0-9][0-9][0-9]')
		if (r.match(clinical_data_df['DOB'][ind])):
			pass
		else:
			totalErrors+=1;
			DOBErrors += 1;
	
	variableMetaData.insert(2, "Errors", [0, DOBErrors, 0, 0, siteOfOnsetErrors, elEscorialErrors, 0, onsetToDiganosisErrors, 0, 0, 0, dementiaErrors, C9orf72Errors], True) 
	print(variableMetaData)



if __name__ == '__main__':
	run()


