import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LinearRegression
# import mglearn
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np
# from sklearn.linear_model import Ridge
filename="C:/Users/PRASHUN/Desktop/django/mysite/nagarro/static/crop_production.csv"
df=pd.read_csv(filename)
df["Productivity"]=df["Production"]/df["Area"]
df=df.dropna()
# print df['Crop'].value_counts()
# print df["State_Name"].value_counts()
# dfuttar=df.loc[df['State_Name'] == 'Uttar Pradesh']
# dfmadhya=df.loc[df['State_Name'] == 'Madhya Pradesh']
# dfKarnataka=df.loc[df['State_Name'] == 'Karnataka']
# dfBihar=df.loc[df['State_Name'] == 'Bihar']
# dfAssam =df.loc[df['State_Name'] == 'Assam']
# dfOdisha=df.loc[df['State_Name'] == 'Odisha']
# dfTamil=df.loc[df['State_Name'] == 'Tamil Nadu']
# dfMaharashtra=df.loc[df['State_Name'] == 'Maharashtra']
# dfRajasthan=df.loc[df['State_Name'] == 'Rajasthan']
# dfChhattisgarh=df.loc[df['State_Name'] == 'Chhattisgarh']
# dfAndhra=df.loc[df['State_Name'] == 'Andhra Pradesh']
# dfWest=df.loc[df['State_Name'] == 'West Bengal']
# dfGujarat=df.loc[df['State_Name'] == 'Gujarat']
# dfHaryana=df.loc[df['State_Name'] == 'Haryana']
# dfTelangana=df.loc[df['State_Name'] == 'Telangana']
# dfUttarakhand=df.loc[df['State_Name'] == 'Uttarakhand']
# dfKerala=df.loc[df['State_Name'] == 'Kerala']
# dfNagaland=df.loc[df['State_Name'] == 'Nagaland']
# dfPunjab=df.loc[df['State_Name'] == 'Punjab']
# dfMeghalaya=df.loc[df['State_Name'] == 'Meghalaya']
# dfArunachal=df.loc[df['State_Name'] == 'Arunachal Pradesh']
# dfHimachal=df.loc[df['State_Name'] == 'Himachal Pradesh']
# dfJammu=df.loc[df['State_Name'] == 'Jammu and Kashmir']
# dfTripura=df.loc[df['State_Name'] == 'Tripura']
# dfManipur=df.loc[df['State_Name'] == 'Manipur']
# dfJharkhand=df.loc[df['State_Name'] == 'Jharkhand']
# dfMizoram=df.loc[df['State_Name'] == 'Mizoram']
# dfPuducherry=df.loc[df['State_Name'] == 'Puducherry']
# dfSikkim=df.loc[df['State_Name'] == 'Sikkim']
# dfDadra=df.loc[df['State_Name'] == 'Dadra and Nagar Haveli']
# dfGoa=df.loc[df['State_Name'] == 'Goa']
# dfAndaman=df.loc[df['State_Name'] == 'Andaman and Nicobar Islands']
# dfChandigarh=df.loc[df['State_Name'] == 'Chandigarh']
# dataframes={"Uttar Pradesh":dfuttar,"Madhya Pradesh":dfmadhya,"Karnataka":dfKarnataka,"Bihar":dfBihar,"Assam":dfAssam,"Odisha":dfOdisha,
#            "Tamil Nadu":dfTamil,"Maharashtra":dfMaharashtra,"Tamil Nadu":dfTamil,"Rajasthan":dfRajasthan,"Chhattisgarh":dfChhattisgarh,"Andhra Pradesh":dfAndhra,
#             "West Bengal":dfWest,"Gujarat":dfGujarat,"Haryana":dfHaryana,"Telangana":dfTelangana,"Uttarakhand":dfUttarakhand,"Kerala":dfKerala,
#             "Nagaland":dfNagaland,"Punjab":dfPunjab,"Meghalaya":dfMeghalaya,"Arunachal Pradesh":dfArunachal,"Himachal":dfHimachal,"Jammu and Kashmir":dfJammu,
#             "Tripura":dfTripura,"Manipur":dfManipur,"Jharkhand":dfJharkhand,"Mizoram":dfMizoram,"Puducherry":dfPuducherry,"Sikkim":dfSikkim,"Dadra and Nagar Haveli":dfDadra
#            ,"Goa":dfGoa,"Andaman and Nicobar Islands":dfAndaman,"Chandigarh":dfChandigarh}

# dataframes["Andaman and Nicobar Islands"].head()

def getCrops(stateName):
	fig=Figure()
	ax = fig.add_subplot(111)
	dfx=df.loc[df['State_Name'] == stateName]
	a=dfx[["Crop","Productivity"]].groupby('Crop').mean().sort_values(['Productivity'], ascending=False).plot(ax=ax)
	canvas = FigureCanvas(fig)
	return canvas

