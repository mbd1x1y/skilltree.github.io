# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 10:27:17 2024

@author: shender
"""

initial_ratings = {'BOR': 600,'CTB': 300,'DHR': 200,'KEM': 450,'MRD': 600,'MRD(B)': 100, 'PAN': 250,
                   'TIL': 500,'TNF': 600,'TNF(B)': 100,'SWS': 250, 'NDT': 150,'RDT': 200, 
                   'DGC': 1000,'SLG': 1200,'SDA': 650,'MCM': 900,'CRD': 450,'DIS': 450,'PSO': 350,
                   'CWB': 425,'RCR': 425,'PIT': 300,'CBB': 400,'PHH': 250,'AUA': 200,'TOM': 300,'CAB': 300,
                   'FLC': 100,'CHK': 250,'DEM': 80,'TRD': 50,'CLG': 50,'PIT(B)': 40,'CBB(B)': 40,'SDA(B)': 120,
                   'SLG(B)': 180,'CAB(B)': 40,'CRD(B)': 100,'PHH(B)': 150}


team_names = {
    'AUA': 'Austin Anarchy',
    'CWB': 'Carolina Wreckingballs',
    'CAB': 'Casco Bay Roller Derby',
    'CAB(B)': 'Casco Bay (B)',
    'CBB': 'Chicago Bruise Brothers',
    'CBB(B)': 'Chicago (B)',
    'CHK': 'Chinook City Roller Derby',
    'CLG': 'Cleveland Guardian\'s Roller Derby',
    'DGC': 'Denver Ground Control',
    'DEM': 'Detroit Men\'s Roller Derby',
    'DIS': 'Disorder',
    'FLC': 'Flour City Roller Derby',
    'CRD': 'Concussion Roller Derby',
    'CRD(B)': 'Concussion Roller Derby (B)',
    'MCM': 'Magic City Misfits',
    'PHH': 'Philadelphia Hooligans',
    'PHH(B)': 'Philadelphia Shenanigans (B)',
    'PIT': 'Pittsburgh Roller Derby',
    'PIT(B)': 'Pittsburgh ZomBees (B)',
    'PSO': 'Puget Sound Outcast Derby',
    'RCR': 'Race City Rebels',
    'SDA': 'San Diego Aftershocks',
    'SDA(B)': 'San Diego Tremors (B)',
    'SLG': 'St. Louis Gatekeepers',
    'SLG(B)': 'St. Louis B-Keepers (B)',
    'TRD': 'Terminus Roller Derby',
    'TOM': 'Toronto Men\'s Roller Derby',
    'BOR': 'Borderland Bandits Roller Derby',
    'CTB': 'Crash Test Brummies',
    'DHR': 'DHR Men\'s Roller Derby',
    'KEM': 'Kent Men\'s Roller Derby',
    'MRD': 'Manchester Roller Derby',
    'MRD(B)': 'Manchester (B)',
    'NDT': 'Nordicks de Touraine',
    'PAN': 'Panam Squad',
    'RDT': 'Roller Derby Toulouse',
    'TIL': 'The Inhuman League',
    'TNF': 'Tyne and Fear Roller Derby',
    'TNF(B)': 'Tyne and Fear (B)',
    'SWS': 'South Wales Silures',
}

gamecount_active = {key: 0 for key in team_names}

team_gp_dict = {key: [] for key in team_names}
