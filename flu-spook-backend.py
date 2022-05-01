{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "29789c33",
   "metadata": {
    "_cell_guid": "7116f93f-c13a-439a-b9b0-2c72eb4de977",
    "_uuid": "ab4acca2-ecff-4086-8354-8b6d9a1175af",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:09.896274Z",
     "iopub.status.busy": "2022-05-01T20:48:09.895808Z",
     "iopub.status.idle": "2022-05-01T20:48:21.543483Z",
     "shell.execute_reply": "2022-05-01T20:48:21.542586Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 11.670585,
     "end_time": "2022-05-01T20:48:21.545923",
     "exception": false,
     "start_time": "2022-05-01T20:48:09.875338",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: statsmodels==0.13.2 in /opt/conda/lib/python3.7/site-packages (from -r ../input/requirements/requirements.txt (line 1)) (0.13.2)\r\n",
      "Requirement already satisfied: fbprophet in /opt/conda/lib/python3.7/site-packages (from -r ../input/requirements/requirements.txt (line 2)) (0.7.1)\r\n",
      "Requirement already satisfied: sklearn in /opt/conda/lib/python3.7/site-packages (from -r ../input/requirements/requirements.txt (line 4)) (0.0)\r\n",
      "Requirement already satisfied: pandas in /opt/conda/lib/python3.7/site-packages (from -r ../input/requirements/requirements.txt (line 5)) (1.3.5)\r\n",
      "Requirement already satisfied: matplotlib in /opt/conda/lib/python3.7/site-packages (from -r ../input/requirements/requirements.txt (line 6)) (3.5.1)\r\n",
      "Requirement already satisfied: patsy>=0.5.2 in /opt/conda/lib/python3.7/site-packages (from statsmodels==0.13.2->-r ../input/requirements/requirements.txt (line 1)) (0.5.2)\r\n",
      "Requirement already satisfied: numpy>=1.17 in /opt/conda/lib/python3.7/site-packages (from statsmodels==0.13.2->-r ../input/requirements/requirements.txt (line 1)) (1.21.6)\r\n",
      "Requirement already satisfied: packaging>=21.3 in /opt/conda/lib/python3.7/site-packages (from statsmodels==0.13.2->-r ../input/requirements/requirements.txt (line 1)) (21.3)\r\n",
      "Requirement already satisfied: scipy>=1.3 in /opt/conda/lib/python3.7/site-packages (from statsmodels==0.13.2->-r ../input/requirements/requirements.txt (line 1)) (1.7.3)\r\n",
      "Requirement already satisfied: Cython>=0.22 in /opt/conda/lib/python3.7/site-packages (from fbprophet->-r ../input/requirements/requirements.txt (line 2)) (0.29.28)\r\n",
      "Requirement already satisfied: cmdstanpy==0.9.5 in /opt/conda/lib/python3.7/site-packages (from fbprophet->-r ../input/requirements/requirements.txt (line 2)) (0.9.5)\r\n",
      "Requirement already satisfied: pystan>=2.14 in /opt/conda/lib/python3.7/site-packages (from fbprophet->-r ../input/requirements/requirements.txt (line 2)) (2.19.1.1)\r\n",
      "Requirement already satisfied: LunarCalendar>=0.0.9 in /opt/conda/lib/python3.7/site-packages (from fbprophet->-r ../input/requirements/requirements.txt (line 2)) (0.0.9)\r\n",
      "Requirement already satisfied: convertdate>=2.1.2 in /opt/conda/lib/python3.7/site-packages (from fbprophet->-r ../input/requirements/requirements.txt (line 2)) (2.4.0)\r\n",
      "Requirement already satisfied: holidays>=0.10.2 in /opt/conda/lib/python3.7/site-packages (from fbprophet->-r ../input/requirements/requirements.txt (line 2)) (0.13)\r\n",
      "Requirement already satisfied: setuptools-git>=1.2 in /opt/conda/lib/python3.7/site-packages (from fbprophet->-r ../input/requirements/requirements.txt (line 2)) (1.2)\r\n",
      "Requirement already satisfied: python-dateutil>=2.8.0 in /opt/conda/lib/python3.7/site-packages (from fbprophet->-r ../input/requirements/requirements.txt (line 2)) (2.8.2)\r\n",
      "Requirement already satisfied: tqdm>=4.36.1 in /opt/conda/lib/python3.7/site-packages (from fbprophet->-r ../input/requirements/requirements.txt (line 2)) (4.63.0)\r\n",
      "Requirement already satisfied: scikit-learn in /opt/conda/lib/python3.7/site-packages (from sklearn->-r ../input/requirements/requirements.txt (line 4)) (1.0.2)\r\n",
      "Requirement already satisfied: pytz>=2017.3 in /opt/conda/lib/python3.7/site-packages (from pandas->-r ../input/requirements/requirements.txt (line 5)) (2021.3)\r\n",
      "Requirement already satisfied: fonttools>=4.22.0 in /opt/conda/lib/python3.7/site-packages (from matplotlib->-r ../input/requirements/requirements.txt (line 6)) (4.30.0)\r\n",
      "Requirement already satisfied: cycler>=0.10 in /opt/conda/lib/python3.7/site-packages (from matplotlib->-r ../input/requirements/requirements.txt (line 6)) (0.11.0)\r\n",
      "Requirement already satisfied: pyparsing>=2.2.1 in /opt/conda/lib/python3.7/site-packages (from matplotlib->-r ../input/requirements/requirements.txt (line 6)) (3.0.7)\r\n",
      "Requirement already satisfied: kiwisolver>=1.0.1 in /opt/conda/lib/python3.7/site-packages (from matplotlib->-r ../input/requirements/requirements.txt (line 6)) (1.4.0)\r\n",
      "Requirement already satisfied: pillow>=6.2.0 in /opt/conda/lib/python3.7/site-packages (from matplotlib->-r ../input/requirements/requirements.txt (line 6)) (9.0.1)\r\n",
      "Requirement already satisfied: pymeeus<=1,>=0.3.13 in /opt/conda/lib/python3.7/site-packages (from convertdate>=2.1.2->fbprophet->-r ../input/requirements/requirements.txt (line 2)) (0.5.11)\r\n",
      "Requirement already satisfied: hijri-converter in /opt/conda/lib/python3.7/site-packages (from holidays>=0.10.2->fbprophet->-r ../input/requirements/requirements.txt (line 2)) (2.2.3)\r\n",
      "Requirement already satisfied: korean-lunar-calendar in /opt/conda/lib/python3.7/site-packages (from holidays>=0.10.2->fbprophet->-r ../input/requirements/requirements.txt (line 2)) (0.2.1)\r\n",
      "Requirement already satisfied: typing-extensions in /opt/conda/lib/python3.7/site-packages (from kiwisolver>=1.0.1->matplotlib->-r ../input/requirements/requirements.txt (line 6)) (4.2.0)\r\n",
      "Requirement already satisfied: ephem>=3.7.5.3 in /opt/conda/lib/python3.7/site-packages (from LunarCalendar>=0.0.9->fbprophet->-r ../input/requirements/requirements.txt (line 2)) (4.1.3)\r\n",
      "Requirement already satisfied: six in /opt/conda/lib/python3.7/site-packages (from patsy>=0.5.2->statsmodels==0.13.2->-r ../input/requirements/requirements.txt (line 1)) (1.16.0)\r\n",
      "Requirement already satisfied: joblib>=0.11 in /opt/conda/lib/python3.7/site-packages (from scikit-learn->sklearn->-r ../input/requirements/requirements.txt (line 4)) (1.0.1)\r\n",
      "Requirement already satisfied: threadpoolctl>=2.0.0 in /opt/conda/lib/python3.7/site-packages (from scikit-learn->sklearn->-r ../input/requirements/requirements.txt (line 4)) (3.1.0)\r\n",
      "\u001b[33mWARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv\u001b[0m\u001b[33m\r\n",
      "\u001b[0m"
     ]
    }
   ],
   "source": [
    "!pip install -r '../input/requirements/requirements.txt'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "a4ac13f7",
   "metadata": {
    "_cell_guid": "5bac5311-49c3-48ad-aa38-da4c658a341e",
    "_uuid": "75ca929c-2aef-4d99-8fa8-fe282c6a9dca",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:21.587186Z",
     "iopub.status.busy": "2022-05-01T20:48:21.586880Z",
     "iopub.status.idle": "2022-05-01T20:48:21.590764Z",
     "shell.execute_reply": "2022-05-01T20:48:21.590013Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.026461,
     "end_time": "2022-05-01T20:48:21.592498",
     "exception": false,
     "start_time": "2022-05-01T20:48:21.566037",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "# Running\n",
    "#! python -m streamlit run your_script.py\n",
    "# is equivalent to:\n",
    "#! streamlit run your_script.py"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "5182d11f",
   "metadata": {
    "_cell_guid": "a852b358-fe77-4b87-a2be-a05ffc631619",
    "_uuid": "e733a3b3-5440-4153-977a-4dd201a8c287",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:21.632363Z",
     "iopub.status.busy": "2022-05-01T20:48:21.632095Z",
     "iopub.status.idle": "2022-05-01T20:48:22.052117Z",
     "shell.execute_reply": "2022-05-01T20:48:22.051299Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.442793,
     "end_time": "2022-05-01T20:48:22.054539",
     "exception": false,
     "start_time": "2022-05-01T20:48:21.611746",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "from pandas import read_csv\n",
    "from pandas import to_datetime\n",
    "from fbprophet import Prophet\n",
    "\n",
    "# load data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "863fd22c",
   "metadata": {
    "_cell_guid": "c59a040c-a38a-4e32-9e12-5e4734dadd0d",
    "_uuid": "5763c950-d20e-4c45-bcda-8fc6a2ba4347",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:22.095887Z",
     "iopub.status.busy": "2022-05-01T20:48:22.095573Z",
     "iopub.status.idle": "2022-05-01T20:48:22.100134Z",
     "shell.execute_reply": "2022-05-01T20:48:22.099327Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.027532,
     "end_time": "2022-05-01T20:48:22.102166",
     "exception": false,
     "start_time": "2022-05-01T20:48:22.074634",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "import warnings\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import pickle\n",
    "warnings.filterwarnings(action='ignore')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1d1076b9",
   "metadata": {
    "_cell_guid": "f07da693-7445-423a-8535-4bb7ad99fc77",
    "_uuid": "f8ed3e63-2532-48a3-9a25-eb4aeaa6f9cd",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:22.142082Z",
     "iopub.status.busy": "2022-05-01T20:48:22.141816Z",
     "iopub.status.idle": "2022-05-01T20:48:22.316802Z",
     "shell.execute_reply": "2022-05-01T20:48:22.315978Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.197194,
     "end_time": "2022-05-01T20:48:22.318793",
     "exception": false,
     "start_time": "2022-05-01T20:48:22.121599",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Year</th>\n",
       "      <th>Week</th>\n",
       "      <th>SDATE</th>\n",
       "      <th>AH1</th>\n",
       "      <th>AH1N12009</th>\n",
       "      <th>AH3</th>\n",
       "      <th>AH5</th>\n",
       "      <th>ANOTSUBTYPED</th>\n",
       "      <th>INF_A</th>\n",
       "      <th>BYAMAGATA</th>\n",
       "      <th>...</th>\n",
       "      <th>Country_New Zealand</th>\n",
       "      <th>Country_Papua New Guinea</th>\n",
       "      <th>Country_Philippines</th>\n",
       "      <th>Country_Republic of Korea</th>\n",
       "      <th>Country_Singapore</th>\n",
       "      <th>Country_Viet Nam</th>\n",
       "      <th>WHOREGION_Western Pacific Region of WHO</th>\n",
       "      <th>FLUREGION_Eastern Asia</th>\n",
       "      <th>FLUREGION_Oceania Melanesia Polynesia</th>\n",
       "      <th>FLUREGION_South-East Asia</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>EDATE</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2022-02-27</th>\n",
       "      <td>2022</td>\n",
       "      <td>8</td>\n",
       "      <td>2022-02-21</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-03-06</th>\n",
       "      <td>2022</td>\n",
       "      <td>9</td>\n",
       "      <td>2022-02-28</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-03-13</th>\n",
       "      <td>2022</td>\n",
       "      <td>10</td>\n",
       "      <td>2022-03-07</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-03-20</th>\n",
       "      <td>2022</td>\n",
       "      <td>11</td>\n",
       "      <td>2022-03-14</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2022-03-27</th>\n",
       "      <td>2022</td>\n",
       "      <td>12</td>\n",
       "      <td>2022-03-21</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>5 rows × 34 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            Year  Week      SDATE  AH1  AH1N12009  AH3  AH5  ANOTSUBTYPED  \\\n",
       "EDATE                                                                       \n",
       "2022-02-27  2022     8 2022-02-21  0.0        0.0  0.0  0.0           0.0   \n",
       "2022-03-06  2022     9 2022-02-28  0.0        0.0  0.0  0.0           0.0   \n",
       "2022-03-13  2022    10 2022-03-07  0.0        0.0  0.0  0.0           0.0   \n",
       "2022-03-20  2022    11 2022-03-14  0.0        0.0  0.0  0.0           0.0   \n",
       "2022-03-27  2022    12 2022-03-21  0.0        0.0  0.0  0.0           0.0   \n",
       "\n",
       "            INF_A  BYAMAGATA  ...  Country_New Zealand  \\\n",
       "EDATE                         ...                        \n",
       "2022-02-27    0.0        0.0  ...                    0   \n",
       "2022-03-06    0.0        0.0  ...                    0   \n",
       "2022-03-13    0.0        0.0  ...                    0   \n",
       "2022-03-20    0.0        0.0  ...                    0   \n",
       "2022-03-27    0.0        0.0  ...                    0   \n",
       "\n",
       "            Country_Papua New Guinea  Country_Philippines  \\\n",
       "EDATE                                                       \n",
       "2022-02-27                         0                    0   \n",
       "2022-03-06                         0                    0   \n",
       "2022-03-13                         0                    0   \n",
       "2022-03-20                         0                    0   \n",
       "2022-03-27                         0                    0   \n",
       "\n",
       "            Country_Republic of Korea  Country_Singapore  Country_Viet Nam  \\\n",
       "EDATE                                                                        \n",
       "2022-02-27                          0                  0                 1   \n",
       "2022-03-06                          0                  0                 1   \n",
       "2022-03-13                          0                  0                 1   \n",
       "2022-03-20                          0                  0                 1   \n",
       "2022-03-27                          0                  0                 1   \n",
       "\n",
       "            WHOREGION_Western Pacific Region of WHO  FLUREGION_Eastern Asia  \\\n",
       "EDATE                                                                         \n",
       "2022-02-27                                        1                       0   \n",
       "2022-03-06                                        1                       0   \n",
       "2022-03-13                                        1                       0   \n",
       "2022-03-20                                        1                       0   \n",
       "2022-03-27                                        1                       0   \n",
       "\n",
       "            FLUREGION_Oceania Melanesia Polynesia  FLUREGION_South-East Asia  \n",
       "EDATE                                                                         \n",
       "2022-02-27                                      0                          1  \n",
       "2022-03-06                                      0                          1  \n",
       "2022-03-13                                      0                          1  \n",
       "2022-03-20                                      0                          1  \n",
       "2022-03-27                                      0                          1  \n",
       "\n",
       "[5 rows x 34 columns]"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data=pd.read_csv(\"../input/flureports/WPOFluNetInteractiveReport.csv\", parse_dates=['EDATE'], index_col='EDATE', skiprows=3)\n",
    "data.tail(1)\n",
    "\n",
    "data = data.fillna(0) #fill any remaining gaps with 0\n",
    "_=data.pop('SPEC_RECEIVED_NB') #remove the number of specimen received\n",
    "_=data.pop('SPEC_PROCESSED_NB') #remove the number of specimen processed\n",
    "data['SDATE'] = pd.to_datetime(data['SDATE']) #from object to datetime\n",
    "data.head()\n",
    "\n",
    "target=data.pop('TITLE')\n",
    "one_hot_encoded_data = pd.get_dummies(data)\n",
    "one_hot_encoded_data.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "07c1cd5d",
   "metadata": {
    "_cell_guid": "8ecc0cee-8838-4934-90f9-d68d69b9f8b8",
    "_uuid": "a36940f6-7f4e-4638-bbde-1d0ead362a04",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:22.360518Z",
     "iopub.status.busy": "2022-05-01T20:48:22.359916Z",
     "iopub.status.idle": "2022-05-01T20:48:24.555052Z",
     "shell.execute_reply": "2022-05-01T20:48:24.554140Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 2.218979,
     "end_time": "2022-05-01T20:48:24.557733",
     "exception": false,
     "start_time": "2022-05-01T20:48:22.338754",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Influenza trend'}, xlabel='EDATE'>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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iARAyRMRmdKcc+xo2pEsw7W2ci2NXY1pbaZnT2dZ2bJksuS4GccRDoWDCVhERERERERERERGnZInIjKlOOfY3bw7LVlS11mX1iY/K5/T5pyWLMN1/MzjyQrpf5eBUPkzEREREREREREJgEYDRWRSc86xr3VfsgzX2oq1VHdUp7XJDeeydM5SVpavZGX5SpbMWkJ2KDugiEVERERERERERCRoSp6IyKRT0VrBmso1ydklFW0VafuzQ9mcMvuUZBmuk2efTE44J6BoRUREREREREREZLxR8kREJryqtqq0Mlz7Wvel7c+yLE6afVKyDNcps08hLysvoGhlMFS0S0REREREREREgqDkiYhMOLUdtT1luCrXsrt5d9r+sIVZMnNJMlmydM5SpmVPCyhaERERERERERERmWiUPBGRca+hsyEtWbKjaUfa/pCFWFy6OFmGa1nZMqZnTw8oWhEREREREREREZnolDwRkXGnqauJdVXrkgmT1xpeO6jNcTOOS84sWVa+jKKcogAilVGnul0iIiIiIiIiIhIAJU9EJHAt3S1sqNqQnFmytX4rDpfW5uiSo5PJkuVlyynJKwkmWAlES30nt3/1GcoWFvGBrywPOhwREREREREREZnklDwRkTHXHmlnQ7WfLKlYy+b6zcRdPK3NwuKFyTJcy8uWMzN/ZkDRSpASE082/nUPAFU7m4MLRkREREREREREpgwlT0Rk1HVEO9hYvTFZhuuV2leIumhamwWFC5IzS1aUr2D2tNkBRSvjkYv3zER68bG9nHLe4QFGIyIiIiIiIiIik52SJyIy4rpiXWyq2cSayjWsqVjDptpNROPpyZJ5BfPSkiXl08sDilYmgs3PVCSf//03ryl5IiIiIiIiIiIio0rJExEZtkgswku1LyXXLNlYvZHueHdam7JpZclEycq5K5lXMC+gaGVCMa9wVywS76ehiIiIiIiIiIjIyBlU8sTMrgHeDywGOoBngK8457altMkDfgB8GMgFVgNXO+eqUtr8GHgTcCKwxTm3tJdrnQysAlYANcBPnHPfH0y8IjI6IvEIr9S+wrqqdaypWMPGmo10RDvS2szKn5WcWbKyfCWHFx6OmfVxRpG+NVa1Bx2CiIiIiIiIiIhMMYOdefJmvITGWv/Y7wIPm9kJzrk2v831wEXAxUATcAPwe7xkSapbgDcAJ2dexMyKgIeBR4CrgJOAW8ys0Tl30yBjFpFhisVjbKnf4pXhqlzDC1Uv0B5NH9AuzStledlyb3bJ3BUsLFqoZImMiKfvfT3oEEREREREREREZIoZVPLEOfe21NdmdjlQDSwDnjKzYuATwCXOucf8NlcAW8zsjc655/zzfM7fN5tekifApUAOcKVzrht4xcyWAl8ClDwRGWVxF2db/bZkGa71VetpjbSmtSnOLWZ52fLk7JKjS45WskQGLBaLEwpZv/9mzCAeVckuEREREREREREZW8Nd86TY/1nv/1wGZOPNGAHAObfVzPYApwPPDfC8pwNP+YmThNXAV8xshnOuIfMAM8vFKxOWUDjAa4lMeXEX5/XG11lbuZY1FWtYV7WO5u7mtDaF2YUsK1uWXLPk2BnHErJQQBHLRNbZFuHmL/8NgM/8/LyAoxERERERERERETnYkJMnZhYCfgg87Zx72d9cDnQ75xozmlf5+waqHNjZyzkS+w5KngDXAN8YxDVEpiznHDubdibLcK2rXEdDV/p/VtOypnFa2WnJNUsWly4mHAoHFLFMJvtf7e1/4SIiIiIiIiIiIuPHcGaerMJb8P3MEYpluK4Frkt5XQjsCygWkXHFOceelj1eGa6KtaytWkttR21am/ysfE6dcyorylewonwFJ8w8gexQdkARi/Roa+ruv5GIiIiIiIiIiMgIGlLyxMxuAN4JnO2cS01QVAI5ZlaSMfukzN83UJX+ManKUvYdxDnXBXSlxDiIy4lMPvta9nlluPzZJdXt1Wn7c8O5LJ29NFmG68SZJ5IdVrJExpdYzFG3v7X/hjKlmNnZwL/ilQudC7zPOXd/yv5bgcsyDludunabmZUCPwHeBcSBe4HPO+daU9qcjHezyAqgBviJc+77o/CWREREZAJRX0RERGRqGFTyxLyMxE+A9wHnOOcyS2utByLA+Xgf/JjZccAC4NlBXOpZ4L/NLNs5F/G3XQhs6229ExGByrZKL1FS4S3yfqDtQNr+7FA2J88+mZXlK1lRvoKTZ59Mbji3j7OJjA/RrljQIcj4NB14EbgF+H0fbR4Crkh53ZWx/y68wY4L8dZr+xVwE3AJgJkVAQ/jreN2FXAScIuZNTrnbhqZtyEiIiITlPoiIiIiU8BgZ56swvsgfw/QYmaJdUyanHMdzrkmM7sZuM7M6oFmvGTLs8655GLxZnY0UIC3fkm+mS31d232F4m/G2/9kpvN7Ht45cE+D3xxKG9SZDKqaa/xynD5s0v2tuxN259lWZw468TkzJJTZp9CflZ+QNGKePa8UsdDN77cf0ORQ3DOPQg8CIecadrlnOt1tqqZHQ+8DVjhnFvnb/ss8Bcz+xfn3AHgUiAHuNLvm7zi91e+hDewISIiIlOU+iIiIiJTw2CTJ5/2fz6Rsf0K4Fb/+RfpmXKaC6wGrs5o/0vgzSmvX/B/LgR2+UmYt+Ala9YDtcC3dHeFTGW1HbWsq1rH2govWbKreVfa/pCFWDJziZcsKV/JqXNOZVr2tGCCFenDn37yYtAhyNRxjplVAw3AY8B/Oufq/H2nA42JwQrfI3j9lzcA9/ltnvIHKxJWA18xsxm9zYQ1s1y8vk9C4Yi9GxEREZlo1BcRERGZ4AaVPHHO9buQiHOuE/iM/+irzTkDOM8m4KzBxCcymTR2NrK2am2yDNf2pu1p+w1jceliVpavZOXclZw25zQKcgoCilZEZFx5CK+Exk5gEfBd4EEzO905F8Ob+Zq2EJRzLurPmk3Mqi33j09VlbKvtzKi1+DNnBUREZGpTX0RERGRSWBIC8aLyMhr7m5mXeW6ZBmuVxtePajNsTOOTa5ZsqxsGcW5xQFEKhK8V/62nyVnzQs6DBmnnHP3pLx8ycw2AduBc4BHR/HS1wLXpbwuBPaN4vVERERkHFJfREREZHJQ8kQkIK3drWyo3sCaijWsqVzD1vqtOFxam0XFi5JrliwvW86MvBkBRSsyvjxx1zYWnTaHvOnZQYciE4BzboeZ1QJH4w1YVAJzUtuYWRZQ6u/D/1mWcaqylH29XaeLlMVgD1EDXURERKYQ9UVEREQmJiVPRMZIe6SdF6pfSC7yvrluMzEXS2tzZNGRyTVLlpcvZ1b+rICiFRn/1j24i1efr6SjJcKnf3ouoZC+HErvzGw+MBOo8Dc9C5SY2TLn3Hp/23lACHg+pc1/m1m2cy7ib7sQ2NZbjXERERGRvqgvIiIiMjEpeSIySjqjnWys2Zhcs+Tl2peJumham8MLD2dF+YpkwmTOtDl9nE1k4vvll54a0fNFu2J0tHjfI3e/XMfCk5VsnCrMrADvzs2EhWa2FKj3H98A7sW7K3MR8H3gdbxFVnHObTGzh4BfmNlVQDZwA3CPc+6Af867/fPcbGbfA04EPg98cXTfnYiIiIx36ouIiIhMDUqeiIyQ7lg3L9a8mFyzZFPNJiLxSFqbudPnJhd4X1G2grkFcwOKVmTgnHNU7WymbGHRsKb+d7VH+280RPFYfNTOLePScuDxlNeJ2t63AZ8GTgYuA0qAA8DDwNf8UhYJl+INUjwKxPEGOD6X2OmcazKztwCrgPVALfAt59xNo/B+REREZGJRX0RERGQKUPJEZIgisQgv172cnFmysWYjXbGutDZzps3xkiX+Iu/zCuap7qxMOL/73nqqd3nJkw98ZXnQ4YjgnHsCONT/TN86gHPUA5f002YTcNagghMREZFJT30RERGRqUHJE5EBisajbK7bnFyz5IXqF+iIdqS1mZk300uUzPXKcC0oXKBkiUx41buaAaja2TzgY158dC9//+1rfPhrK5k5r2C0QhMRERERERERERkVSp6I9CEWj7G1YStrK7wyXBuqN9AWaUtrMyN3BsvLlydnlywsXqhkiQjw99++BsBjt2/h4mtWjMo14nE3KucVERERERERERFR8kTEF3dxXmt4jTWVa1hTuYb1Vetp6W5Ja1OUU8TysuXemiXlKzi65GhCFgooYpHxLxoZvbVItjxdkXy+fX01i06dM2rXEhERERERERGRqUXJE5mynHO83vh6sgzXuqp1NHU1pbUpyC5gWdkyVpR7ZbiOnXEs4VA4oIhFJp76A239NxoBr62r5i2fHJNLiYiIiIiIiIjIFKDkiUwZzjl2Nu9MluFaV7WO+s76tDb5WfmcVnZasgzX4tLFZIX0n4nIYDincloiIiIiIiIiIjKxaVRYJi3nHHtb9ibLcK2rXEdNR01am7xwHkvnLPUWeS9fwZJZS8gOZQcUscjk8OKje9NeO+e0FpCIiIiIiIiIiEwoSp7IpLK/dT9rKrwyXGsq11DVXpW2PyeUwylzTkmW4Tpp1knkhHMCilZkcnr6d6+nva54vYnDjikJJhgREREREREREZEhUPJEJrTKtspkomRt5Vr2t+5P258VyuLkWScnkyWnzDmF3HBuQNGKTHy7X67jiBNnDuqYJ3+9jY98/Q2jFJGIiIiIiIiIiMjIU/JEJpTajlrWVKxJJkv2tOxJ259lWSyZtSRZhmvpnKXkZ+UHFK3I5FO5o2nQyZOxWjReRERERERERERkpCh5IuNafWc9ayvXJmeX7GzambY/ZCFOKD2BFXO9mSWnzTmNadnTAopWZHJpqe/k9q8+MyLn2rB694icR0REREREREREZCwoeSLjSlNXE+sq1yUXeX+9MX3tBMNYXLo4WYbrtLLTKMwpDChakfFl1VWPAfBPP34zWTnhYZ9vpBInAK+tq+q/kYiIiIiIiIiIyDih5IkEqqW7hfVV65NluLbVb8Ph0tocM+OYZBmu5WXLKc4tDihakfGrubYj+fzGzz3JZ35+XoDRiIiIiIiIiIiITGxKnsiYaou0saFqQ7IM15b6LcRdPK3NUcVHJWeWLC9fTmleaUDRikwc8bjrv5GIiIiIiIiIiIgMiJInMqraI+1srNmYTJa8UvsKMRdLa3NE0RHJZMmK8hXMyp8VULQi0p/UGS6DUbu3dYQjERERERERERERGT1KnsiI6ox28mLNi8kyXC/VvkQ0Hk1rM69gXjJRsrJ8JWXTywKKVkQG69U1VSx+41wOP0EzwkREREREREREZPJS8kSGpTvWzaaaTcmZJZtqNtEd705rUz69PC1ZcljBYQFFKyKHklhw/tOrziEUDvXZbvMzB5Q8ERERERERERGRSU3JExmUSDzCK7WvsKZyDWsq1/Bi9Yt0xjrT2szOn51MlKwsX8n8wvmYWUARi8hg1e5rZc4RRX030PIqIiIiIiIiIiIyySl5IocUjUfZUrclWYZrQ/UGOqLpax6U5pUmZ5asKF/BkUVHKlkiMsF1tkWCDkFERERERERERCQwSp5Imlg8xraGbckyXBuqNtAaSV/ouSS3JJkoWVm+kqOKj1KyRCRoIzgbxMUhFo33vV8zT0REREREREREZJJT8mSKi7s4rzW8lkyWrKtaR0t3S1qbwpxClpctT84uOWbGMYSs7/UQRGRsdXdGuesbz6Vtu/2rz/Dx754xpPP97nvrRiIsERERERERERGRCUvJkynGOceOph3JMlxrK9fS2NWY1mZ69nSWlS1LJkuOm3Ec4VA4mIBFpF8HXms8aFtLfefBDUeMpp5IsMzsbOBfgWXAXOB9zrn7/X3ZwHeAdwBHAU3AI8C/O+cOpJxjF3BExqmvcc79T0qbk4FVwAqgBviJc+77o/OuREREZKJQX0RERGRqUPJkknPOsbt5d1qypK6zLq1NflY+p805LVmG6/iZx5MV0j8NEemDcicSvOnAi8AtwO8z9k0DTgO+7beZAfwI+COwPKPt14FfpLxOTr00syLgYbzBjquAk4BbzKzROXfTiL0TERERmYjUFxEREZkCNEI+yTjn2Ne6L1mGa23FWqo7qtPa5IZzWTpnKSvLV7KyfCVLZi0hO5QdUMQiIiKD45x7EHgQOGjNLedcE3Bh6jYz+2dgjZktcM7tSdnV4pyr7OMylwI5wJXOuW7gFTNbCnwJ0ICFiIjIFKa+iIiIyNSg5MkkcKD1QNrMkoq2irT92aFsTpl9SrIM18mzTyYnnBNQtCIyVqp2NVN2ZNGIn1cTT2QCKsb7p9uYsf3fzexrwB7gbuB651zU33c68JQ/WJGwGviKmc1wzjVkXsTMcoHclE2FIxS/iIiITGzqi4iIiExASp5MQFVtVclkyZrKNexv3Z+2P8uyOGn2SckyXKfMPoW8rLyAohWRoLQ1dgUdgkjgzCwP+B7wa+dcc8quHwMbgHrgDOBavJrlX/L3lwM7M05XlbLvoAEL4BrgGyMTuYiIiEwG6ouIiIhMXEqeTAC1HbU9Zbgq17K7eXfa/rCFWTJzSTJZsnTOUqZlTwsoWhGZ9Mbp1JOK1xuZe3RJ0GHIOOIv2PobwIBPp+5zzl2X8nKTmXUDN5rZNc65oWYerwVSz1sI7BviuURERGSCU19ERERkYlPyZBxq6GxIS5bsaNqRtj9kIRaXLk6W4VpWtozp2dMDilZEZHyo2NGk5IkkpQxWHAGcl3GnZ2+ex+sXHQlsAyqBsow2ide91ib3BzqSgx2ZNdBFRERk6lBfREREZOJT8mQcaOpqYl3VumTC5LWG1w5qc9yM45IzS5aVL6MoZ+TXMRARGQjnxunUExFfymDFMcC5zrm6ARy2FIgD1f7rZ4H/NrNs51zE33YhsK23GuMiIiIiCeqLiIiITA5KngSgpbuFDVUbkjNLttZvxWXUwTm65GhWlq/0kiVlyyjJKwkmWBGZsKp2NlNYmkfR7Hxy8yf//+4N3Vk3VZhZAXB0yqaFZrYUr2Z4BfA74DTgnUDYzMr9dvXOuW4zOx14A/A40IK3IOv1wJ0pgxF349UMv9nMvgecCHwe+OJovjcREREZ/9QXERERmRom/2jaONAeaWdDtZ8sqVjL5vrNxF08rc3C4oXJMlzLy5YzM39mQNGKyGSxYfVuNqz21ki6+qfnYqFJnlyY5G9P0izHG2xISNT2vg34JvBu//XGjOPOBZ7AK2fxYb9tLt5irNennAfnXJOZvQVYBawHaoFvOeduGrF3ISIiIhOV+iIiIiJTwKCSJ2Z2DfB+YDHQATwDfMU5ty2lTR7wA7yOQC6wGrjaOVeV0mYB8DO8jkMrXgfjGudcNKXNOXgdhyXAXuA7zrlbB/sGg9AR7WBj9cZkGa5Xal8h2vPWAFhQuCBZhmtF+QpmT5sdULQiMhW89OR+Tj53/oicS1W7JGjOuSc4dLrskKk059wG4I0DuM4m4KxBBSciIiKTnvoiIiIiU8NgZ568Ge+uh7X+sd8FHjazE5xzbX6b64GLgIuBJuAG4PfAmwDMLAw8gLfA2RnAXOB2IAJ81W+z0G/zc+BS4Hzgl2ZW4ZxbPaR3Ooq6Yl1sqtnEmso1rKlYw6baTUTj6cmSeQXz0pIl5dPL+zibiMjI2/ZcxYglT0bSw798mbd88sQROVdTTceInEdERERERERERGRQyRPn3NtSX5vZ5XiLmS0DnjKzYuATwCXOucf8NlcAW8zsjc6554C3ACcAF/izUTaa2deA75nZN51z3cBVwE7n3Jf9S20xszPxansGnjyJxCK8VPtScs2SjdUb6Y53p7Upm1aWTJSsnLuSeQXzAopWRGT8em1dNUsvbGbOEUXDPtcrT+1nxwvVXP69MwlN9hJlIiIiIiIiIiIyqoa75kmx/7Pe/7kMyAYeSTRwzm01sz14C6A95/98KbWMF15C5Gd4Jbpe8Ns8QrrVwA+HGe+Q7W/dz4M7H2RNxRo21mykI5p+h/Os/FnJmSUry1dyeOHhmGnwTkSkP7+9dh2nXHA4Z37gmGGfq6Mlwk2fe5ITzjqMsz907AhEJyIiIiIiIiIiU9GQkydmFsJLZjztnHvZ31wOdDvnGjOaV/n7Em2qetnPANoUmVm+c+6g2ixmlou3xkpC4cDeycDsad7Djzb8KPm6NK+U5WXLvdklc1ewsGihkiUiMjWMwqInuzbVjkjyBCAWjfPS4/uUPBERERERERERkSEbzsyTVcCJwJkjFMtwXQN8Y7ROvnTOUi484kKWlS1jZflKji45WskSEZFxrLmug6KZ+UGHISIiIiIiIiIiE1BoKAeZ2Q3AO4FznXP7UnZVAjlmVpJxSJm/L9GmrJf9DKBNc2+zTnzX4pURSzxGdGXk/Kx8rjvnOi49/lKOmXGMEiciMmXteqmOuv2tQYfRr6fueTXoEEREREREREREZIIaVPLEPDcA7wPOc87tzGiyHogA56cccxywAHjW3/QscJKZzUk57kKgGdic0uZ80l2Yco6DOOe6nHPNiQfQMpj3JiIiA3fPt9fw6K2b+28YoN0v1bHnlbqgwxARERERERERkQlosDNPVgEfBS4BWsys3H/kAzjnmoCbgevM7FwzWwb8CnjWOfecf46H8ZIkd5jZKWb2VuA7wCrnXJff5ufAUWb2fTNbbGZXAx8Erh/GexURkT5U7mga9DHbN9aMQiQjq3qP8ugiIiIiIiIiIjJ4g02efBqvJNYTQEXK40Mpbb4I/Bm4F3gKrwTX+xM7nXMxvJJfMbyZJHcCtwNfT2mzE7gIb7bJi8CXgU8651YPMl4RERmAjX/dM+hjIp0xGqvbRyEaERERERERERGRYA1qwXjnXL8LfTjnOoHP+I++2uwG3tHPeZ4ATh1MfCIiMrbu+vpzzDuuhHf+8ylkZYeHfJ6m6r6WsxIRERERERERERl7Q1owXkREJGH/tkZeeHjwM1d601ynJIqIiIiIiIiIiARvUDNPREREelN/oG3Y51h11WMA5E3PHva5EvZtqWf5248csfOJiIiIiIiIiMjUoJknIiIyfP0WdRy4zrbIiJ1r/6uN/PmGF0fsfCIiIiIiIiIiMjUoeSIiMgVU724Zk+tsfbZiTK4zGLtfrgs6BBERERERERERmWBUtktERIYtMfHk0du2BBpHX+KxOKGw7hcQERGRsRXv6qLt2WexcBa5i44i+7DDgg5JRERERAZIyRMREWH7CzXDO4GNYN2uUfC337zGmz9yXNBhiIiIyBRT94tfUnvDDd6LcJhFq1eTM39esEGJiIiIyIDoNlwRkSli79Z6/v6b14IOIxB1+1qDDkFERESmoLa//73nRSxG947twQUjIiIiIoOimSciIlPEH3+4EYC5xxSz6NQ5wQYjIiIiMsnFOzvpeOUVALLnzSOyfz+xpuaAoxIRERGRgdLMExGRKaahsn3EzznOq3aJiIiIjLnOl1+GSITw7FnknXACALEWJU9EREREJgolT0REpjjnXNAhiAyKmZ1tZn8yswNm5szsvRn7zcy+ZWYVZtZhZo+Y2TEZbUrN7C4zazazRjO72cwKMtqcbGZ/M7NOM9trZv82Bm9PREQmifYNLwAw7dTTCBUXARBvVvJkMlBfREREZGpQ8kREZIp5/g870l4/9etXh33OV9dU8dCNLw37PCIDNB14EfhMH/v/DfgccBXwBqANWG1meSlt7gKWABcC7wTOBm5K7DSzIuBhYDewDPhX4Jtm9qkRfSciIjJpdaxfD0D+aacSLioGUNmuyUN9ERERkSlAa56IiExxFdsbR+Q821+oGZHziPTHOfcg8CCAZdSMM2/DF4DvOOf+4G/7OFAFvBe4x8yOB94GrHDOrfPbfBb4i5n9i3PuAHApkANc6ZzrBl4xs6XAl0gZ2BARkamje99+smbNJJSX129bF4/TvnEjANOWLaPt6acBle2aLNQXERERmRo080REREQmk4VAOfBIYoNzrgl4Hjjd33Q60JgYrPA9AsTx7g5NtHnKH6xIWA0cZ2YzeruwmeWaWVHiARSOxBsSEZHgdW3fzvYLL2T/l748oPbdO3YQb2rC8vPJW7yYUJFftkszT6YC9UVEREQmCSVPREREZDIp939WZWyvStlXDlSn7nTORYH6jDa9nSP1GpmuAZpSHvsGE7iIiIxfHS+9BM7RtXXrgNp3btsGQN7ixVh2NuFCL3kSa2lJtnGRCN379FExCakvIiIiMkkoeSIiMgV1tkaCDkFkMroWKE55zA82HBERGSmRAwcAiDY0DKh9965dAOQsXAhA2F8wPtbclGxTde21bL/gQtqee34EI5UpTn0RERGREaTkiYjIFPT4XQO7a1JkAqr0f5ZlbC9L2VcJzEndaWZZQGlGm97OkXqNNM65Ludcc+IBtPTWTkREJp7I/v0AuI4O4h0d/bbv3rUbgJwjjwQgVOhVT4o393w0tD37HABd29Qvm2TUFxEREZkklDwREZmCdrxQQzwWJxqJBR2KyEjbiTegcH5ig1/z+w3As/6mZ4ESM1uWctx5eP2i51PanG1m2SltLgS2OecGdtuxiIhMKC4W48B//ie1P/vZQfsSM08AYvX1/Z4rOfPkyCMACBcXe8c2e2uexDs66N7tJViijY3DCVvGH/VFREREJomsoAMQEZFg/Oa7a6mvaCevILv/xiLjiJkVAEenbFpoZkuBeufcHjP7IfCfZvYa3gDGt4EDwP0AzrktZvYQ8AszuwrIBm4A7nHOJUbH7ga+AdxsZt8DTgQ+D3xxlN+eiIgEpGPTJpp+dy+EQsz8xCewnJzkvsj+nuRJtL6B7Hnz+jyPcy6ZGEnMPAknZp60tODicbpe3w7xOAAxJU8mHPVFREREpgYlT0REpqi6/W0AdDR3BxyJyKAtBx5PeX2d//M24HLg+8B04CagBPg78DbnXGfKMZfiDVI8CsSBe4HPJXY655rM7C3AKmA9UAt8yzl308i/HRERGQ86NrzgPYnHiVRUkHOEN2vE+a8TYg2HnnkSa2gg7s8wyVmwAICQP/ME54i3tqaV6lLyZEJSX0RERGQKUPJEREREJhTn3BOAHWK/A77uP/pqUw9c0s91NgFnDS1KERGZaNpf2JB83r1vXzJ5Eq2pgUgkuS/aT9muRMmurMPmEsrLAyCUk4Pl5eE6O4k1N9O57dVkeyVPJh71RURERKYGrXkiIiIiIiIiU5pzjo4XNiZfR/bu63meUrILIFZ/6OUmunfuAiDXL9mVkCzd1dxM17ZtPedrbBpCxCIiIiIy2pQ8ERGRSa9iuwYlREREpG+RPXuI1dX1vN6fmjzZn9a2v7JdmeudJISKi7zjM5MnDVr7W0RERGQ8UvJEREREREREprT2xHonvu59KcmTA+kzTwZatiszeRIu9JInXa++Rqyp58YOle0SERERGZ+UPBEREREREZEpreMFL3mSWOcksq9ntkli5kl49ixgAGW7EskT/1wJ4SIvedK+bh0AWeXlALjOTuKdnWlt452d3lorIiIiIhIYJU9ERERERERkSuvYtAmAone9C4DI3r3JfYmZJ/knngRA7BAzT5xzdO/ZAxycPAklkidr1gAwbdkyyMryzpky+8TF4+y54kpeP/8CulPiEBEREZGxpeSJiIiIiIiITGmJBEnBmW8CvGRGrLXN2+fPPMk7cQkA0UOsURKrr8d1doIZ2YcdlrYvMfMkkSjJP/kkwsXFadsAmv/yIB0vvIDr7qbtueeG+c5ERERkouveu5fKb32bvVd/5qByojK6soIOQERERERERCQo8fZ24s3NAOQsWkS4pIRYYyOR/fsILVzYM/PkpP5nnkQqKgHImjULy8lJ2xcqKkx7nXfyyd616uqSyRPX3U3Nj36UbNO5efPw3pyIiIhMWJ3btlH3i1/S/Je/QDwOwK6XX+bwX/yCvOOODTi6qUHJExEREREREZmyIlVVAISmTSNUUED2/Ple8mTvXmINjbiuLsIzZ5LnJ0/ira3Eu7sJZSRHACIVXqIla+7cg/aFi4p7XmRnk3fCCYRLSgCI+bNZGu+9N61kmJInIiIiU0/7+vXU3nQTbU8+ldw2/cwziVRW0P36dnZfeinzV61i+htWBhjl1KCyXSIiIiIiIjJlRf3kSVZZGWZG9vz5AHTv20frU96gRcFZZ3kltsJhoCfZcdC5/Jkn2b0mT3pmnuQtXkwoN5fwjBLvfI2NuEiEul/8EoAZH/sYAF1bt+Gi0eG+RRERERnnnHO0PP44uy65lN2XftRLnIRCFL79bSz8/b0s+OUvOPKuu8hfvox4ayt7P/lJmh98MOiwJz0lT0RERERERGTKSiZPyssAyDncS55E9u6j9aknASh489lYKER4xgyg79JdkYoKALLLyw/al1gwHiD/5JMBemaeNDbS/NBDRA4cIFxaypwvfoHQ9Om4ri66duwY7lsUERGRccpFozT96U/sfPd72Pfpq+nYsAHLzqbkgx9k0V8eYP7115N3wgkAhIuLWXDzzRReeCEuEmH/l75M/e23B/wOJjeV7RIREREREZEpK1JVDUD2HC95knv00QA03X8/8bY2CIeZfsYZAGTNmEGstpZoX8mTSj95ctihy3bln+IlT7L85Em0oYHmv3h3j5Z+/OOEpk0j7/jjaV+3js7Nm8k7VnXNRUREJpN4ZyeNv/899TffQmT/fsArIVrykQ9TetllZM+Z0+txodxc5v3weqr++7s03H03Vd+9lkhVFXO+/GUspHkSI03JExEREREREZkUunbsoPaGVVhuLnmLj2PGxz+OmR3ymGilv8i7P1uk6O1vp/6uu+nctAmA/FOXeiW7gHBpKQCx+j7Kdh2o8M916LJdmTNPWh95lMiBA4SmT2fGJR8BIG/JCV7y5JXN8N739vveRUREZPyLNTfTcPevqb/99uRM1nBpKaUf/xgzPvKRZJ/jUCwcpuxr/0lWWRk1119P/c23EK2u4bD//g7Wy5psMnRKnoiIiIiIiMiE03j//TTccSfzrvsBOUccAUDNj35My+rVADQBeUuWMG358kOeJ1KdWPPEu8PTcnKYd9117Hz/+4k3N1Nw9puTbcOlftmuhr5mnvhrnvQy8yR77lwsO5us2bPJ9uNNJE8iB7yF5gvf8hbCfnmvvCVLAC0aLyIiMhlEqqtpuP12Gn59jzezFcg+7DBKP3ElJe9/P6H8/EGdz8yY9U+fImvOHCq+9jWa//QnYnW1zPvxTwgXTB+NtzAlKXkiIiIiIiIiE0q0pobKb30b195O3a23Mvcb3yDW2kbrE08A3uLv0aoqunbu7Dd5Eq30kifZZWXJbTnz53H4z39O8wMPJGeCAGSVzgQg4i8Mn8pFIkSr/RJgvax5Ei4pYeF9vyc0fXpyNkxiDZWEgrPPSj7PXbwYgK5XXz1k/CIiIjJ+de/eTd3Nt9B03324SASA3GOOZuY//iNFb387lp09rPOXvO+9ZM2ayb7Pf4G2Z55l98c/xoIbbyRr9uyRCH/KUyE0ERERERERmVBqfnIDrr0dgJYHH8J1d9P62KO4ri5yjjySwvPPA7xF3/uTXDC+LD3hMe20Uyn/2n8SLihIbstfuhSA1iefPPg81dXgHJadTXjmzF6vlXv00WTP7ZmVkph5AkAolFxbBUgOesRbWnDRaL/vQ0RERMaPzs2b2f+lL7H97e+g8Te/wUUi5J96KvN/9lMW/uEPFL/73cNOnCQUnHUWR9x2G+GZM+navIVdH/4IXTt3jsi5pzolT0RERERERGTC6Nq+ncbf/Q7wFlaNNTbS+venaX7gLwAUveMdZM8/HIDIvkMnT1wkQrS2FoDsst4XZk1VcO45WHY23Tt20PX662n7IhWJ9U7KB7xga2ryJH/p0rQ656lJm3hr64DOJyIiIsHq3rOHfZ/7PDvf/w80/+VBiMeZ/uazOeLOOzji7rsoPPfcUVnYPf+kEzny13eTvWABkf372f2RS+h48cURv85Uo+SJiIiIiIiITBitTz7lDUSceSYlF18MQN2NN9L69NMAFF30DrIPnw9Adz/Jk2htLTgHWVl9zhZJFS4oYNoZpwPQ8te/pu1LlPJKnVnS7/lSkicFZ52Zts+ys7Fp0wCItbQM+JwiIiIy9mKNjVRdey3bL3onLQ8/DKEQRRddxML772PBjTcybfnyZNnO0ZKzYAFH/vpu8k48kVhjI7svu5yWxx8f1WtOdoNOnpjZ2Wb2JzM7YGbOzN6bsb/MzG7197eb2UNmdkxGm0Vmdp+Z1ZhZs5n9xszKMtqUmtld/v5GM7vZzAoQkRER7+qi+aHVOOeCDkVEREREZMAi+/YCkHfCCRS9+10A3p2V0Sj5p5xC7qJF5BzuzzzZu/eQ50qW7Joze8B3gRa95S0AND+cmTzxZp5kzz14vZO+hIuLIRwGYPpZZx+83599EmtuHvA5RUREZOy47m7qbr2V19/6Nupvux0iEaafeSYL77uPeT/4X/L8NczGStbMmRxx261MP/ssXGcn+z7zzzT89rdjGsNkMpQF46cDLwK3AL9P3WFe+ux+IAK8B2gGvgQ8YmYnOOfazGw68LB/jvP8Q78N/MnM3uici/vb7gLmAhcC2cCvgJuAS4YQs4hk2HbKUgCK3v0u5n3/+8EGIyIiIiIyQInZJNmHz/cSKO94O51btlL41rdQ+vGPe/vmezNPYg0NxFrbCBdM7/VckeRi8QNPeBScdx6Ew3Rt2ULXjp2E8vOouvZ/kgu7Zw1i5ollZVF2zTXE6uvJW3LCQftDRYVQXU28RWW7RERExhPnHC0P/5XqH/yAyJ49AOQecwxz/u3fDppNOtZC06dz+KpVVHz9GzTddx+VX/s60epqZl199ajPfplsBp08cc49CDwI9PbLPgZ4I3Cic+4Vv82ngUrgI8AvgTcBRwKnOuea/TaXAQ14yZRHzOx44G3ACufcOr/NZ4G/mNm/OOcODDZuEeld+9p1QYcgIiIiIlNEvKuLtqefYdryZYSLioZ0jsi+/QDkzJ+PmTHvuusOahMuKCBcUkKssZHI/n2Ejzuu13NFqxOLxZf1ur83WTNmUHDWWbQ+8QS1N9xArLWFtqf+ltyfmPUyUKUfvbTPfeFC73cUa9HMExERkfGi48UXqfre9+nYsAGA8OxZzP7c5yh5//sxf0Zp0Cw7m7nf/W+yyuZQ9/Mbqf3JDUSrqin/+tewrKHMp5iaRnrNk1z/Z2digz+TpAs4M6WN87eR0j6e0uZ0oDGROPE94rd5Q28XNrNcMytKPIDCYb4XkSkhHu/qv5GIyARiZrv80qKZj1X+/id62ffzjHMsMLMH/BKk1Wb2/8xMPUwRkWGqv+129l19Na+ufAP1d9416OOdc0T2e8mTxOySvmQfnr5ofOvfn6bqe98nWlOTbNO5eYvXdhDJE4DZn/8cmNH8l794iZPsbGZ+6lPM/MdPUvSOdwzqXIcSKvTKdsWbtebJRKK+iIjI5NS9bz/7v/Rldn3ow3Rs2IDl5THr6qs5+qGHmHHxxeMmcZJgZsz5whco/8bXwYzG3/yGfZ/7PPGOjqBDmzBG+oN3K7AHuNbM/gloA74IzMcrwQXwnL/9e2b2VcCA/wHCKW3KgerUEzvnomZW7+/rzTXAN0burYhMDdFIY9AhiIiMtBV4/YqEE4G/AqmFXn8BfD3ldXviiZmFgQfwZs6egdc/uR2vLOlXRydkEZGpIVpZmXxe9Z3vkH/iEvKXLh348TU1uK4uCIXILj90qa3s+fPofOklunfupPLb36HhLi9Z0/Looyy45WaIx2n6858BKHzrWwb1PvKOP56id72T5j/+CYCZV1zBnC99cVDnGIjEzJN4q5InE4z6IiIik0isuZnaG2+k4fY7cJEImFH83vcy+wufH/QNGEGY8ZGPEJ41iwNf/hdaH3uMPVdcyfyf/ZSsGTOCDm3cG9GZJ865CPB+4FigHu/D/1y8Ml9xv00NcDHwLqAVaAJKgA2JNkN0LVCc8jj0bUgiAnjTwESmotobb2L3Rz8WdBgyCpxzNc65ysQDeCewHXgypVl7aptEKVHfW4ATgI865zb6JUu/BnzGzHLG7I2IiExCmXc6drz08qCOT5Tsyi4vx7KzD9k2Z74386T2Zz9PJk7CJSVE9uxh1wc/xIF//TeIRpl+1llMO+20QcUBMOfznydUWEj2ggXMuuqfBn38QISKvIIKMc08mVDUFxERmRxcJEL9nXex/S1vpf7mW3CRCNPe+EYW/v5eDrv2uxMicZJQdOGFLPjVLYSKi+nYuJHdl1xKt9+vkr6NdNkunHPrnXNL8RIic51zbwNmAjtS2jzsnFsEzAFmOec+BsxLaVPp70vyp6eW+vt6u26Xc6458QDUuxQRkT7VXH897evW0fbcc0GHIqPIH2D4KHCLcy41X3ypmdWa2ctmdq2ZTUvZdzrwknOuKmXbaqAIWHKIa6mEqIhIPxLJk1CBV46q6/XXAXDxgd1HF9nvLxbfT8ku8BaUB4i3tQEw93+uZeEf/kDucccRq6+n48UXAZj9+c8P4h2knH/ePBY9vJqFv7+X0LRp/R8wBFrzZOJTX0REZOJxztHy2GPsePd7qPrOd4g1NpKzaBHzf/4zFvzqFvKOPz7oEIdk2rJlHHnXnWTNnUv3zp3s+siH6dyyJeiwxrURT54kOOeanHM1ZnYMsBz4Qy9tap1zjWZ2Hl6y5I/+rmeBEjNbltL8PD/e50crZhERmXqiNbVBhyCj6714N3TcmrLtbrxBjHPxZq5+DLgzZX85kDpYQcrrQ9WIuQZvRm3isW9oIYuITF7xDq8yUf7JJwFe8qRj0ya2nbKUul/+st/ju/fuBQaWPMlJaTP9jNMpfs97yC6bw8Lf/oY5X/kKWWVlzLj0UvJP7HMsul9ZM2YQ9hNBoyG55klL66hdQ0bde1FfRERkwuh4+RX2XHY5+67+DN07dxIuLaX8G1/nqD/cT+E552BmQYc4LLlHH82R9/ya3GOPJVZTy55//BTxzs7+D5yiBr3miZkVAEenbFpoZkuBeufcHjO7GKjBW/vkJOBHwP3OuYdTznEFsMVvd7rf5nrn3DYA59wWM3sI+IWZXQVkAzcA9zjnDgz+bYpIX8L1w6mWJyIy7n0CeDC1/+Ccuyll/0tmVgE8amaLnHPbh3Gta4HrUl4XokELEZE0rsP7cp534km0PfMsXa+/TtP9f8BFIrQ+8SQzP/nJQx6fKNuVc/gAkicLF3pPsrIo++pXk4MdlpPDzCsuZ+YVlw/9jYwRzTyZFNQXERGZACIVFdT88Ic0/cG7t99ycii9/HJmfuofR/VGiSBkl5VxxF13svO97yOyfz9N9/+BGR/+UNBhjUtDWTB+OfB4yuvEB/NtwOV4C5ldB5QBFXiLmn074xzH4X2olwK7gP8Grs9ocylewuRRvLVQ7gU+N4R4RaQf7evXM23Zsv4bikwS8e7uoEOQMWBmRwAX4K3HdiiJWa1H49UjrwRWZrRJFLPttXwoeCVEga6U6w8mXBGRKSFRtivvhBMgFCLe1ETzX7377CIVFf0eH9k3iLJdc+dy2A/+l3BRMblHH91v+/Eo7K95EteaJxOS+iIiIuOfc47an/6Uupt+gevy/hda9K53MeeLXyD7sMMCjm70hAsLKb3s41R991rqb7uNkg9ejIVGrUjVhDXo5Ilz7gmgz09g59yPgR/3c45/B/69nzb1wCWDjU9EBq9p7/NKnsiUUn/bbUGHIGPjCqAaeKCfdkv9n4lRu2eB/zCzOc65an/bhUAzsHmkgxQRmUoSZbvCJSXkHH443bt3E/NLaEaqq3GxGBYO93l8Mnkyr//kCUDxRRcNM+JghQr9BeNblDyZoNQXEREZ51off5zan9wAQP7yZZR95Svkn3RSwFGNjeL3/wM1P7mB7p07aX3ySQrPPTfokMYdpZNEhFisPegQRMaU6oZPfmYWwhuwuM05F03ZvsjMvmZmy8zsSDN7N94s2aecc5v8Zg/jDUzcYWanmNlbge8Aq/w7OkVEZIhcu79g/LR8co7JmA0SiRCtrev72EiESKV30332/HmjFuN4EvaTJ3ElTyYc9UVERCaGltWrASj50Ic44o47pkziBCBcMJ2SD14MQP2tusm0N0qeiIiIyGR0AbAAuCVje7e/72FgK/ADvNKg70o0cM7FgHcCMbw7P+/EG9T4+qhHLSIyySUWJLW8PHIXHVxKK1rR9xKX7es3QDxOaNo0smbPHrUYx5NQUWLNEyVPJiD1RURExjkXidDyxJMAFL/rnVOy3GHpRz8K4TDtzz9P52ZNbsw0lDVPRERERMY159zD9FJm1Dm3F3jzAI7fDbxjFEITEZnSEmuehKZNS1+HxAycI1JZSX4fx9bd5K2xXfze906ZwY3UmSfOuSnzvicD9UVERMa/9nXriDc1ES4tJf/UU4MOJxDZc+dS9La30fzAA9Tdeivzvv/9oEMaVzTzREREppy2p58OOgQREZEpx8XjuETyJD+f3JSyXdPe+AYAIgd6Fo2PVFUR9xdu7XjpJdqeeQbCYUqvvHIMow5WYs0T4nHibSq1KyIiMpJaHnkUgILzzj3kmmuTXenllwPQ/JcHkyVSxaPkiYiITDmdr7zS5z7n3BhGIiIiMnW4rp6lGkJ5eeQeeywlF1/MrKs/Tf6SJQBEKr3kScfGjWy/4EK2v/VtNP35ASq/+V8AFL/zneRMkfVOACw3F8vOBiDe0hxwNCIiIpOHc46WR73kSeH55wccTbDyTzqRacuXQzRKw113BR3OuKLkiYiIiG/VVY/x008/TmdbJOhQREREJp1EyS4Ay8/HQiHmfvtbzP7c58iaOxeAaIWXPKn5yQ24SIRoZSUH/uVf6HzlFULTpjHzn/4pkNiDYmY96540a90TERGRkdL58itEKyuxadOYfsYZQYcTuNIrrwCg4f9+Q7ytLeBoxg8lT0REZEqL7N9/0LZdL9UGEImIiMjkFm/3kieWl4eF0r+KZvvJk8iBCjo2bvRKbGZlUfiWtwBQcO65LPzD/eQetXBsgx4HkuuetCp5IiIiMlJaHnkEgIKzziKUmxtwNMErOOccco44gnhzM42/vy/ocMYNJU9ERGRKq/7hD4MOQUREZEpwHd6aHaH8g5eETyZPKiup+elPASh+z7uZ/+Mfcey6dRz+s5+Sc/jhYxfsOJJY9yTWrLJdIiIiI6XlUS95UnjBBQFHMj5YKETp5ZcBUH/77bhYLOCIxgclT0REZMp67JxVPH7OKhqrtACriIjIaIt3dgJg+XkH7csqLwcgVldH21N/g3CYWX6JrnDB9LELchxKzjxp0cwTERGRkdC1cyfdr2+HrCwK3nx20OGMG8XveQ/h4mIie/cm14OZ6pQ8ERGRKe/VNZVBhyAiIjLpJcp2hfKnHbQvXFKCpcxIKX7Xu8hZsGDMYhvPtOaJiIjIyGr1EwPT3/AGwv7nrEBo2jRKPvxhAOpvvS3gaMYHJU9ERERERERk1MUPUbbLzJKluwiFmPlPnxrL0Ma1cGEBoDVPRERERkrLXxMlu84POJLxZ8all0B2Nh0bNtDx4otBhxM4JU9ERERERERk1LkOf+ZJ3sFlu6Bn3ZOiiy4id+HUWxi+L6FCzTwREREZKZHq6mRSoOC88wKOZvzJnjOH4osuAqDu1luDDWYcUPJERESmHIcRt6ygwxAREZlS4h3+mifTDp55AjDzE1dS+Ja3MOfLXxrLsMa9cFFizRMtGC8iIjJcrY89BkDeKSeTXVYWcDTjU+kVlwPQsvphuvftDzaYgGnkSEQAqP/13VhuLjPe/w9BhyIy6h4/54agQxAREZlyesp2HbzmCcD0M85g+hlnjGVIE0LIXzA+1qTkiYiIyHC1POKtd1J4/gUBRzJ+5R13HNPPOJ22Z56l4Y47KLvm34MOKTCaeSIixOubqfqvb1P51f8k3t0ddDgiIiIiMgkly3b1suaJ9C2rtBSAWH19wJGIiIhMbLGWFtqefx6AwguUPDmU0iuuAKDxd78j1jJ1S4cqeSIidDdXJZ/H410BRiIy+na+WBN0CCIiIlNSvN1Lnlh+72ueSO/CM7zkSbShIeBIREREJrbWJ5+CSISco44i9yitr3Yo0888k5yjFxFva6Pxt78LOpzAKHkiMgV179qVviEeTz410/8WZHLb9lxl0CGIiIhMSfFOb82Tvsp2Se+yZvozT+rqAo5ERERkYmt59BFAs04GwsyYefnlANTfcQcuGg02oIBolFRkCqr8n/9Oex3tjvW8UPJEpqCmmo6gQxAREZn0etY8UdmuwQgnynY1NU3ZgQsREZHhind10fbkUwAUXnB+wNFMDEXvehfh0lKiFRU0r14ddDiB0CipyBTU2rg17XV3R+qXMBvbYETGgVfXVNHd2fPfwVO/fjXAaERERCYn155Y80RluwYjXFICZuAcscbGoMMRERGZkNqfe454eztZZWXknXhi0OFMCKHcXGZccgkA9b+6FedcwBGNPSVPRKaguIukb5iC//OTqadqZ/Mh9296bF/yeaQrdoiWIiIiMhTxjsSaJ5p5MhgWDnsJFCCqReNFRESGpOURv2TX+edhIQ2JD9SMSz6C5eTQ+fLLdKxfH3Q4Y07/UkQEq2oKOgSRUbf6Fy8fcn80cnDCJBqJseqqx3j8rq29HCEiIiKDEe9MzDyZmmuexOIxPvXwp/jOc98Z9LHhxLonSp6IiIgMmovFaHnscUDrnQxWVmkpxe95DwB1t94abDABUPJERMj6+2vJ5/G4ZqHI5NRbcqQ/Lz2+H4DNfzsw0uGIiIhMOcmyXdMmxsyTh3Y+xCUPXML+1v0jcr5djbt4tuJZfrPtN8RdfFDHZs0YePIk1tJCzapVdO3YOaQ4RUREJpuOjRuJ1dURKipi2ooVQYcz4ZRefhkArY8+RveuXcEGM8aUPBGRNE7JE5GkSFfPOii7XqoNMBIZDDP7ppm5jMfWlP15ZrbKzOrMrNXM7jWzsoxzLDCzB8ys3cyqzez/mVnW2L8bEZHJI1m2K29irHly/+v381LtSzy6+9EROV9NYw0ADkdT5+BmfodnzgQgWtd/8qT5gb9Q+5MbqL3hhsEHKSNCfRERkfGl5RHvs7zgnDdj2dkBRzPx5C5axPQ3nw3OUX/7HUGHM6aUPBGRdPq/gkiv2pu7gw5BBucVYG7K48yUfdcD7wIuBt4MHAb8PrHTzMLAA0AOcAZwGXA58K0xiFtEZNJKJE8mStmu5m5vvbSKtooROV9bV1vyeWVz5aCOzSqdAUCsof/kSbS6CoDuvXsHdQ0ZceqLiIiMA865lPVOVLJrqGZecQUAjffdR6yxMdhgxpCGSUUkjQUdgMgo6WiJBB2CjK2oc64y5VELYGbFwCeALznnHnPOrQeuAM4wszf6x74FOAH4qHNuo3PuQeBrwGfMLCeA9yIiMikk1zyZIGW7WrpbANjXum9EzpeWPGkaXPIkXDrwmSeJAY1I5cgkfWTI1BcRERkHul59jcjevVhODgVnvinocCasaW94A7mLF+M6Omj4v98EHc6YUfJERESmjK3PVbD9hZqgw5CxcYyZHTCzHWZ2l5kt8LcvA7KBRxINnXNbgT3A6f6m04GXnHNVKedbDRQBS/q6oJnlmllR4gEUjuD7EZk04i6OcyoTOhUl1zyZIGW7EjNPDrSOzNpnbd1Dn3kSTsw8GciaJ37yJFZbh+vWzNkAqS8iIjIOtDzyVwCmv+lNhKZPDziaicvMkmufNNx555TpYyh5IiIiU8ajt24JOgQZG8/jlbZ4G/BpYCHwNzMrBMqBbudcY8YxVf4+/J9VvewnpU1vrgGaUh4jc6uyyCQSiUe4+E8Xc+XqK5VAmYKSa55MgLJdzrm05MlI/HvtiHQkn9e2DW4ttaxSb8H46CCSJzhHpLp6UNeREaO+iIjIONHyqLfeSeEF5wccycRX/I53kDV7NtGaGpr+8pegwxkTSp6IiAxR3a9uZcvi49n3xS8GHYqMgcfv2Np/IxkXnHMPOud+65zb5JxbDbwDKAE+OMqXvhYoTnnMH+XriUw4uxt382rDq6yrWkdXrCvocGQMuVgM1+X9zSdC2a7OWCfReBSA1khrMpEyHO2R9uTz2vbBJU/CfvJkIDNPoil1yKMVKt0VBPVFRETGh+59++navAVCIQrOPTfocCY8y8lhxkc/CkD9rbdNiZuhlDwRERmi2htuAKDlwYcCjkREDsW/s/NV4GigEsgxs5KMZmX+PvyfZb3sJ6VNb9fpcs41Jx5AyzBDF5l0tlT0zACsb+9/EFgmD9fZmXweyh//yZPmrvRkyf7W/cM+Z+rMk4bOhkEdO6SZJ0CkcnDlwWR0qC8iIhKM1se8WSfTTjst+VkqwzPjQx/E8vPp2rqV9ueeCzqcUafkiYiICLD+wd1BhyCjxMwKgEVABbAeiADnp+w/DlgAPOtvehY4yczmpJzmQqAZ2DwWMYtMVttrtyef17XWBRiJjLVEyS4Ay80NMJKBSSwWnzAS6550RnsSSI3djYM6NjzTWzA+3tSEi0SS25/a9xQX/PYCnq94Prkt1tiUfB6pUPJkPFBfREQkGC1/9ZaXKrzwgoAjmTzCJSWUvO99ANTdemuwwYwBJU9ERESGaPPTB/jZ1Y/T1R7pv7GMGTP7XzN7s5kdaWZnAPcBMeDXzrkm4GbgOjM718yWAb8CnnXOJW6beRhvYOIOMzvFzN4KfAdY5ZxTnSGRYdjTtCf5vL5VM0+mkp71TvKx0Pj/GtoSSU+ejMjMk2hPAqk5MrgyYOHiYvB/b9GGnlkrj+55lKr2Kp7e/zQA8a4uXHtPebBopcp2BUF9ERGR4EUbGmhfvx6AgvOVPBlJpZd9HMxoe/IpurZv7/+ACWz891pFRMapeFtb0CHIKFv7wK4+9zXVdPD4HVuJxx3P3Pv62AUlAzEf+DWwDfgNUAe80TlX4+//IvBn4F7gKbzyF+9PHOyciwHvxBvkeBa4E7gd+PoYxS8yaR1o77l7X2W7ppZE8mQilOyCg8t2jfTMk5bY4KopWShEeMYMIH3dk9oOb+2URGImtWQXaOZJgNQXEREJWOvjT0A8Tu7xx5Mzf17Q4UwqOUccQcH55wHe2ieTWVbQAYjI2Au/2NTnvnhHB+RNG8NoRCamO7/2bPJ5Z1s0wEgkk3Puw/3s7wQ+4z/6arMbb3FXERlBNV01yeeNHY3BBSJjziWSJ3l5AUcyMJkLxI/EzJPOWE/ypM0N/iacrNIZxOrqiNXX42IxWlavZtFTW+kMxek+0pttclDyRGueBEJ9ERGR4LU84pfsOv/8flrKUMy84gpaH3mUpj/8gdlf+DxZfonRyUYzT0Qkzf7vXxN0CCIiIjIJOedocD3lhho7Gnl639Nc+ecr2du8N8DIZCwky3ZNmyAzT/zkSWF2ITAyyZOuaE+1pQ46cM4N6vhwqTco0fLoY1R89avs/9KXefv9B/iX38c55i+vABBraPQbhwGIVvSU7eret08zp0VEZEqIt7fT9rRX0lLrnYyO/NNOI++kk3Dd3TT8+p6gwxk1Sp6ISJqu+/6G6+4OOoxxb7BfdkVERKa6xs5GItazRlRTVxOr/r6KtXVruWPNHQFGJmMh1uKVqQoXFAYcycAkFow/rvQ4wCvbNdz+X2d3T+IibnHaIoNLZBS9w5uE0HDXXTT94Y8QDrP1cAPgiHVecicx8yT3qIXJ1/GODrpef53tb30b+//tK8N6DyIiIhNB69//juvqInv+fHKPPTbocCYlM6P08ssAaLj7buJdk3NJLiVPROQgXTt3Bh3CuNf2t78FHYKIiMiE8mr1q2mvW7pbqO/y1m7Y3bg7iJBkDMWbvWREqHBiJU8Wly4GoD3aTlNX36VvB6IrpWwXQFVr1aCOn/GhDzL3u9/FsrMhHGbG977N998fIm4wa38rkf37k8mT7MMXEJrmleKNVFbS8dLLEIvR+uSTmn0iIiKTXuujjwJQeMEFmFnA0UxeRW99K1mHzSVWX0/TH/8YdDijYtDJEzM728z+ZGYHzMyZ2Xsz9peZ2a3+/nYze8jMjsloU25md5hZpZm1mdkGM/uHjDalZnaXmTWbWaOZ3WxmBUN6lyIyKLGovlD1J1qnRW5FREQG47Xq19Jet3a30hb3+hw1nTW9HSKTSLzVn3lSODG+0iXKds3Mn5ks3dXQ1XCoQ/rV7SJpryubBr8eScn738dRD/6Fo/74B9rPPIXWacbW+d6+lsceTyZPwiUlZM2dC0C0spJopV++KxqlfcOGIb8HERGR8c5FIrQ8/gQAhRdovZPRZFlZlH70Y4C3cPxkrNIylJkn04EX6WVhM/NSefcDRwHvAU4FdgOPmNn0lKa3A8cB7wZOAn4P/MbMTk1pcxewBLgQeCdwNnDTEOIVkUHq7K4OOoRxz0K6c0FERGQwdtanz2xtjbbSjrfIdX1UNyVMdrGWVgBChUUBRzIwiZknRTlFFOV6MWcuIj9Y3S69NG5V8+BmniTkzJ9P7qJF1HbUArDuGO9rfctjj6YlT7LLywGIHKggUtGTqGl77rkhXVdERGQiaF+3jnhzM+HSUvJPPbX/A2RYSi7+AKHp0+nevn1SVmkZdPLEOfegc+4/nXP39bL7GOCNwKedc2udc9uATwP5wEdS2p0B/MQ5t8Y5t8M59x2gEVgGYGbHA28DPumce94593fgs8CHzeywwcYsIjLiQiNf9XDXRz9KzU9uGPHzysS0++U6Vl31GE/f+3rQoYiIjIh9LfsAmBbxSgm1RFvoDnmDyc2uaVLeqSY94i0Ta+ZJInlSmFNIUY6fPOkaXvIkkph54v9Tr24d3g1LdZ11AKw7xrupp33tOrr37gX85Mnh3pSU7r17iFT1JE/an3t+WNcVEREZz1r++ggABeedi4XDAUcz+YULCyn5wAcAqL/11mCDGQUjPfqX6/9MFnN1zsWBLuDMlHbPAB/yS3OFzOzDQB7whL//dKDRObcu5ZhHgDjwht4ubGa5ZlaUeAATo5iuiExMNrL/+9z5wQ/RsW49tatWjeh5ZeiCHsT7y083AbDxr3vY8YLK2YjIxFfZ6Q3ellkZALWx2uS+SCg67PUkZHxLLBgfmiALxidmmRTlFPUkT4Y58yRCFID8WD4AtW21h2rer8TMk8pSo2J2FkSjtD31FADhkmJyDl/gXXfPXqIpM086N28m1qT/3kREZPJxztGSWO/kfJXsGiulH/8YhEK0PfMsnVu3Bh3OiBrp5MlWYA9wrZnNMLMcM/sKMB+Ym9Lug0A2UIeXWLkReJ9zLnF7bTmQdhuOcy4K1Pv7enMN0JTy2Dci70hEpBddr73Wf6NB6Ny0aUTPJ8P3008/PqzjI90x2pu7+2/Yh3i8J3mz+5W6YcUiIjIeVEe97v3CaQsBaKElbf+O2h1jHpOMncTMk1DRxEiepM48KczxYh5u8iRqXvKkoDsPgPrO4ZWrq+vo6R+8dJR3Z62LeLNbwiUlZC84HIDuvXuJVHrJE8vPB+doX7v2oPO5eJx4Z+dB20VERCaKzpdfJlpVhU2bxvQzzgg6nCkje948Ct/6FsBb+2QyGdHkiXMuArwfOBYv0dEOnAs8iDdrJOHbQAlwAbAcuA5vzZOThnH5a4HilMf8YZxLZGqLq2xGf+puvDHoEGQcqdrVTFdHNG3bTZ97kl/929/paB16AkVEZLJo6mqi1bw1L5aXL/c2ZiwftqNOyZPJLJZcMH5iJE8SJboKcwp71jwZbtkuP3lS3JEDDH8B+sTME4ANC+Np+8IlJeQs8GaedL3+OvFm//34d+F2bHrpoPPVXP9Dtq1YSYdu6hERkQmq5RFv1knBWWcRys3tp7WMpJmXXw5A0wMPEKmaPGspj3jRfufceufcUrzkyFzn3NuAmcAOADNbBPwzcKVz7lHn3IvOuf8C1tGzCH0lMCf1vGaWBZT6+3q7bpdzrjnxgIxb2URkwFoauoIOQWRCaWvs4p5v9V4/vGaPPo5ERDbt9wZj86P5nHD4Cb222dOwZyxDkjEWTywYX3DwmifOOfY07yEajx60LwhxF6c14sU7kmW7ohYDoLzRS57s7do7rPMl1jwBeGl+HEsZJAqXlJAz37uf0HV0ABAqLCT36KO9WGrTS4Y552j6058gEqHpD38cVlwiIiJBaXnEW++k8IILAo5k6sk/5RTyTzsNIhGqrr2WWGtb0CGNiJFf8djnnGtyztWY2TF4s0v+4O+a5v+MZxwSS4nnWaDEzJal7D/P36/V7URGmTvQa45SRA6hVUlHEZE+vbj/RQBmMYs5xXN6bbO/WVV3J7NYi5d46G3myd/2/42L7ruIH6z7wViH1avWSCvOX9U9NXmSKOU1VDE/eXJcRTYAVbEqGjqHPvsktWxXJNvIWXZq8nXWjBmEpk8nPHtWclt2eRlZs2YCEK1LT55E9h8g6pf2anv66SHHJCIiEpSuHTvp3r4dsrIoePPZQYczJc369FUAtDz0EDve/S5a//a3gCMavkEnT8yswMyWmtlSf9NC//UCf//FZnaOmR1lZu8B/grc75x72G+/FXgduNHMVprZIjP7MnAhcD+Ac24L8BDwC7/Nm4AbgHuccweG/nZFZCA6v/ujoEOYUloeeyzoEGSUNVa1s+qqx3juD9v7bRuLqMyXiEw+r9a9CsD8vPmUTi9N22fOq99V2bJ/zOOSsZOceVJYdNC+v+//OwBb6reMaUx9SZTnys/KJzucPSIzT7pj3TjzEjKH1XZT2O0lkTZUbxjyOVOTJwBZb1yefB4uLgZILhoPkFU+l/BML3kSq0lPnnSsX9cT665ddO/Tf48iIjKxtDzqzTqZ/oY3EC46uL8ho6/grLNY8KtbyJ4/n+iBCvb+46c48JV/J9bYGHRoQzaUmSfLgRf8B3jrlbwAfMt/PRe4Ay9J8mP/+UcSB/vrorwDqAH+BGwCPg5c5pz7S8p1LvXP8SjwF+DvwKeGEK+IpNj98cuCDmFYIgcOTIrMdaqu19MH1BMLfcrE01TT3uv2v/3mNQDWP7i7z2Odc6y66jF+/tm/s/aUJaMSn4hIUHa17gJgUcki8vPyyYpnJfeVdHmDvDXdtb0dKkOwq2kXL9e+HHQYSc655ILx4cKDy3a9VOOtv5GZDAhKcrH4bC/BkVzzZBjJk9bO1uTzkqZ2ZnV6M0LWV60f0vniLp5WtgsgfvqpEAqRVV6O5XilwXIOPzy5P7u8nKxZswGI1qUf274uPY62ZzT7REREJpZWf72TwgvODziSqW366adz1B//QOllHwczmv7wB7Zf9E6aH1oddGhDMujkiXPuCeec9fK43N//Y+fc4c65HOfcEc65rznnujPO8Zpz7h+cc2XOuenOuVOcc3dktKl3zl3inCt0zhU75650zrUiIsPSvmZN0CEMy+vnnc/ef/wUHS++GHQoaSq/+90RO1fdr24dsXPJyNr2XAUALfWdve5vqet9eywa6/fcTTUdPc9LzxhCdCIi41dl1CsHtGTW8ez+8EfIiWUn95W1eFV9GxneehLS45MPf5KPPfixtAXFg+S6upI3h4QyynZ1x7rZ2rAVGIfJkxw/eZIz/AXj27r8ut8OSppbmd3pJTGGmjxp7Gok5rz+RU7MS5R0zZvJgpt/yeE/XZVsl72gJ3mSlVq2q74e51xyX/t6L468E0/04n36mSHFJSIiEoRIVXVynKjgPCVPghaaNo2ya67hyF/fTc6iRcTq6tj/hS+w77OfI1I9sRaTH7U1T0RERlPHS+PnbkqAhtvvoO3ZZ0fkXLG68TFwIAd75FavnEjl9qYBH/Pk3dsG1rBn/IJYVm7f7UREJpiatho6rAMcnEApnZs2kRsNJ/cvqPWed4Q66Yh29HUaGaDOaCdV7VVE49FxM/skMesEM0LTp6ft21a/LblQfEukhc5o7zcijKXEDJPEjJORKNvV0unPvHFhprV3JmeebK3bSmv34O8RTCSacmI5yZlcnbFOpp9+OnknnJBsl7Ogp2xXdkrZLiIR4k1efyZaX0/3jh0AzP7sPwPQ9uyzuFj/N3+IiIiMB62Pe+XQ8045meyy3tfXk7GXv3QpC+/7PbOu/jRkZdHy17+y453vovHe36fdxDGeKXkiIjJC9lxxZdAhyDjUXDv4QaDXF71/FCIREQnGxn0bASiIFjCjwpsJkZY8qYokB38rWivGPL7JprGrMfl8a/3W4AJJEUusd1JQgIXSv4Juqt2U9jqzFFUQDpp5MgJluxIzT7LiYcLxOCVtxvTIdOLE2VizcdDnS/yecmO5ZDk/edJL4ikteTK3nFBODiG/Dny01vvvMTHrJPeYY5j+pjdh+fnEm5vp3r3noPM55ybMYIeIiEwdLX/11jspvOCCgCORTKGcHGZ/7nMs/N1vyVuyhHhzMxX/8R/s/cQnJ8Qaa0qeiIhMEK0NXbi492W1vbmbVVc9xqO3beaBVZv6OVLGypo/7+y3TXdnlLr9B99hGunS3Z0iMjltOuB9Ts0Ozab7VW8NqNxIT/LksOYo+dF8APY27B37ACeZhs6G5PPxkjyJt3rJiFAv651kzo4ZD6XGEkmSRPIk8bMt0pacJTNYieRJOO59Bc/v6GBG1wwAdjb13384KEa/hFhOPIdw3J+91cvMrewF6QvGA2T5s0+itV4CpmvbqwDknXwSlpVFzpFHAtC9Kz2uaEMDr59/Pns+fhkuHh90zCIiIqMh1txM2/PPA1B4vpIn41Xe4sUc+X/3MOdf/wXLzaXtmWfY8e53U3/HneO6X6HkiYhMSI3/939BhzCmdr9Sx23XPM1Pr34cgKfu8b7kbn22MsiwJEPF672X89q/rTH5/BdfeIp7vr2Gmr0tdLVHktsfuuml0Q5PRCQQexu9hMjcvLl0bfUG8/Mjltw/r3Qe07u9coV7Gg6+010GZzwmT2LNfsmqgsKD9iWSJyHzvpqOp+RJolxXInkCPbNSBqu9ux2AbD/Rkd/RQX7MSxpWtVUN+nxtkTb/fNmHnHkSLikhf9kychYtIufw+QBkzfJKhkXrvN91957dAMmkSe7Chd72nenJk8Z77iF6oIL2tWtpWb2a5odWs+9zn6d7375Bxy8iIjJSWp/6G0Sj5CxaRO5RC4MORw7BsrKY+YlPsPD++8hfvgzX3k7Vf/83uy/9KF3btwcdXq+ygg5ARGSgXLTnTr+u114LMJKxt3NjTfL5qqseCzASGSl//OFGOtu85Mlnfn7ekMp7iYhMBIkyUqX5pXS++ncA8rv9e7gczF94AgVdNVAAB5rH/9T98a6hqyd5sr91P83dzckkQFB6Zp6kJ0+au5vZ1bwLgKWzl7KhesO4WDQ+WbYrDmz8Ndknf4hpWdNoj7bT3N3MjLwZgz5nW3eibFeI8MyZ5HV0JmdcVbcPfuHURIzZ8ezkLZG9zTwxM4648w6Ix7Gwl7gJ+4vGJ9bZ697tJ08WHOH99JMnXSnJk3h3N/V33Z18XfW973tlv6JRIvv3c+Sv78ZycvqMN97RgeXlYWZ9thERERmKlkf8kl3na6H4iSJ34UKOuP12Gv/v/6j+f/9LxwsvsPO972PWZz7DzE9ciWVnBx1ikmaeiMiE0fi7e4MOYVTE491prxum2KyaqSqROBERmeyao95d/CWh6cT8NRamdXn7cmO5FB23mKJO756uSpXtGrbUmSfgLcgetJi/YHw4I3nyar03k/aw6YdxdMnRwDibebLjKbj/Knjx7p51T7qGtu5JW5dXsjMrFiJ7/jxv5omfPKlqH/zMk9aIf754FmHnJUU6Y73fiGFmycQJQNZMf+aJX7Yr4q9tknOEV+Irx79rt3tHT/Kk+U9/JlZbS9acOYSKiohWVoJ/Y1PnK69Q/YPr+oy17fk1bDv1NOpuvMm7bkNDn21FREQGI97VRdtTTwFQeKFKdk0kFgox4yMf4ag//4npZ5+Fi0So+eEP2fnBD9G5eXPQ4SUpeSIiE0birsXJpnLvk2mvXadmIIgMh5ldY2ZrzazFzKrN7H4zOy6jzRNm5jIeP89os8DMHjCzdv88/8/MNGtXZJBaY94gb3HKTfHTurw1vPKi2WTNmkmJX7arumPwd+BLutSZJzA+SnfFEwvGZyRPXmv0ZhIfM+MYZuV7A/rjIXmSmNVR1Fzhbdj5t+TsnSGX7erwZ4rEjJx589PLdg0jeZIdzyYr7n00tUfaB3Rs1qzEmie1xJqaiDU2ApBz+OFA72W7Gu65B4DSyz7OzCuv8NodfzyH/eB/Aai/7Ta6d+3qPdbHvbKz9XfeiYtG2fvpqwcU50SmvoiIyNhoe/ZZ4u3tZJWVkbdkSdDhyBBkH3YYh994I4d9/3uEi4vp2rKFnRd/kOofXEe8q2tEr+ViMaJ1dXS+/vqAj9GHrohIwLLv1VoXU11359AWn5U+vRlYBazF6+t8F3jYzE5wzrWltPsF8PWU18lRJzMLAw8AlcAZwFzgdiACfHVUoxeZZNribRCC4gbvy0/O0Yso6PD+U5zWnUW4pIQZ0TwA6iL1gcU5WTR2NgKQG86lK9Y1LpInsRZvtkY4Y8H41xu8L67HzDiGmfnegP54Sp4UtvplU/c+T9FxpwI9s1IGq73TT3bEQmSVlZG/cWPazJP/z955h8dRXX34ndm+q1XvxUXuDRsXMKYYU2J6CYQSICEkEEJIICEkJCGEEJKQQggQwhecAoQSugEXbGMMNsa4d1uWrN7LStv7zP3+GGllWZItyTY2ZF49++zOzJ07Z2ZXu3fO755zVKEm6r4MBG9Ys8OkmojL2jiiqyj94TB0FYx3tRGt0aK9jFlZyA4H0F37ROnoIN7RgWyzJWaAJl98McasLMwjRuCYPRtDaiqet98msHoNHa+9Rs699/Y6Xle6XaWtjdbHnyD6v5F+Vx+L6Ojo6HwG+FeuBMB57jlIsh4j8HlFkiRSLrsMx+mn0/Tww/iWvodrwQJ8K1aQ95uHsc+Y0ed+QghUr5e4qx2lo524y4XS3vXcQbzdheJqTzwrbjcIgV9RBmybLp7o6Oj0iRoOI1utx9uMQyIUpUcKghMBIYSey1ln0Lz7xLbjbcIXCiHEBQcuS5J0M9ACzABWH7ApKIRo6qebLwETgfOEEM3ANkmSfgH8XpKkB4UQ0X7209HROYgwWkRlSqMbAOe8eZz8wSI+nZDHrJokDGlpZCp2ANziixll+lnSFXkyI2cGnzR8ckKIJ92RJz1rr3RFnoxOHY3NqAkJJ0LNk67UXE6lc3JDRyXJhtnatqGKJ51pu8yqjCE9DVsohFWxgoC4Gqc93J6IvhkI7QFNaLTJNmJCSwU6UPGkq2C80uZKFIs3dabsApDtdox5ecQbG4lWViHJEigKhowMjDk5SJJE8gXdP7Vp115LYPUaPG++RdZddyEfVPskcsDsTteCBQM+x88z+lhER0dH59gjFAXfSq0mrPM8PWXXFwFjRgaFjz2G7+KLafzVr4hWVVF9w42kXHEFhpQU4u3tKC6X9tzerqUCjQ0+JbohZeD1AHXxREfnf4jAxo0Dbutfs4bk888/htYMnnC8Z7he+7PPkfHNW46TNX0T3rUL25QpR9yPUNUesyaEEEfcp85nQ9AbxZ7cf8HUvmiqGJojRmfApHQ+Hzyl/QZJkm5Em9H5LvBrIUTXjM/TgJ2dzooulgFPA5OArQcfRJIkC2A5YJXz4DY6Ov9rxNQYUVnz7yXt0Opb2E4+mQlvvMk9b5nIaq3E8EAa2bJ2AxOQQkSVKGbD4L5HdbrpqnlSLBfzCZ9Q4a444mvqDrt5ZOMjXDH6CmbnzR70/mqi5kl35IkQokfkSTiuiWyfReTJ6rrVeCIeLh11aZ/bE2m7VDWxLjmq2TdU8SQc1X5eTELGmJ6BLRRCRsaqWAkbw7QEWwYlnnjCHgBS7alEOlNaBGKDE0/iLlevYvFdWEaO6BRPKlEj2rlbJ03sc5JQ0ty5GLOzibe04H//fZIvuiixTfF6iTcflJbsf3NmsD4W0dHR0TnKhLZtQ2lvR05Oxj5r1vE2R+co4jzvPOyzZtH8xz/ief0NPAsXHrK9nJSEISMdY1q6NtkjPV1bTk/HkJ6BMSMdQ3rncmoqvlAIUlIO2WcXuniio/M/hLdly4Dbeha+fcKJJ7tcuxh2wHKssfG42dIfInZ00i+1/fUpsr7/vcRyZN8+YODKuM7xo2JbK5PPKjjeZuh0IkmSDPwFWCuE2HXAppeAaqABOAn4PTAO+HLn9lzg4CT0zQds64ufAr88cqt1dL44tPk6HeECkssbMKSl4ZgzB0t+PsN27QKjETkpiUxzCrIqo8oqLcEWCp2Fx9fwzzFd4knVxiqShyXjjXnZ797PxIyJQ+7z3Yp3WVyxmA9rP+S1S1+jyFk0qP27CsbLSd1+3OZgM76YD6NkZGTySFoD2uT7tlDbMY3kVYXKvR/dSzAeZFjyMKZmTe3VpksgcR4onoTc2rYhFowPx7WiP2bVgDErE0skgiQENsVG2BimOdA8qPeoq+aJ0+LEHddsC0YHWPMkkbbLRSwhngzr0cY8spjAJ+uIVlYkCrz3l0teMhpJvfoq2v72NO7XX+8hnnRFnRizsxGKguJy4TzvXCjdN8Az/fyjj0V0dHR0jg2+Fe8DkHT2XCST6Thbo3O0MaSkkP/ww6RccgneZcswOBwY0jMwpKdhzMjQxJCMDAxpacgWy+E7PJBQ6PBtOvmfnPKho/O/iqoOPLLbv3IlgU8+OYbWDB4h1MM3+pzRX0RJaPeuHsuq3/9ZmKNzlIjHBp4/U+eY8xQwGbjuwJVCiGeEEMuEEDuFEC8CXwOulCRp1BEc63doM0u7Hrr3V+d/niaP5hA3q2bMsThp11+HbLViys8HwJCWiiRJOJKcR1Q8W6ebLvHEoloYZtUc4keauqvCUwFokQ33rb6PmDq49AhdkSfyAZEnZR1ayq4RKSMwNe0g48lTAYiqUXyxY5e+zRvxEoxrIsN/S/7ba3tUiRJWtEiLZFWlvTNgwOnVPpdDjTwJdUbWWIQRY2YmshBYo9EedU8GQ1eUiU04IKKlsR1owfiumifEYoR2amNO8/CDxROtaHykopLwbq3eie0QhXhTLr9cs2vDRhRv9zWKlGrvs2X8ODK/8x3MxcVk3HrrgOz8AqGPRXR0dHSOMkIIfIl6J3rKri8yjtmzyfvlL8n+0Y/IuOUbpF5xBUlnnolt0iRMubmDF04GiS6e6Ojo9Eto1+7jbcIXno4XXuxzfeCj1YgDZjsKoTvjTxTqSg5fzHjT4qpjb4jOYZEk6a/AJcA8IUTdYZqv73we3fncBOQc1CbngG29EEJEhBDergegF2/Q+Z+nudPhbI2bkE0m0q6/HgBTgRahZ0xNA8CektztRA58PsSTmDL4/MrHGlWouKNuACyKhUyhpWc6UvGk0lOZeL2jbQfvVb43qP2VzkkghuTuKNoD651Q8SGWWACn0KJNjmXqrgP7fq/yvV7H6krZJQlIUgXb0ASDZE8DMHTxJKpoqbUswoihM22WNRAYsngSUrQZkx37Y0gRLaFEKD6wWZSyxYLs1KKAohWaMGYe3jNtl3X8OAAC69YlokesE/uPjDEPH4551CiIx/GvWZNY37WvZfQY0m+8gVFLFmMpLh6QnV8E9LGIjs6xRwjB1patickDOv8bREpLidXWIlksJJ15xvE2R+cLjJ62a4C4/BE+3Nfa57b+KhEcqkZBv1sOUdZA9LPxUKUQ+rftszlOfzsdqnpDf8cZyvUc2rUZfG2Jz+p6Hu44Qmj299euoKKdCf130YvyVxfyQvHcIdjS34Yj+zzYWwMceFu3paaD3ctK+m0/0OP0+5nrZw9DJETfGbLhxdWltDZZ+zhG331NX76OEf309dh/PiSQoUXkj/Y1gWlwKTJ0jg0vvribQJa5151sF69tqsXiUxKJrY8GHQG9HuhgkLRcL08CVwJnCyEqD7MLwLTO5658gOuAn0uSlC2EaOlcdz7gBfYcRXN1dL7QtPq18bM1ZsQ5fz7GrCygWzwxpKYCkJSWhq1JcyK3BFt6d3SCsdu1m5uW3MSXRnyJh09/GKN8YtxW+aI+1M5IXbNiRgpoYsTREk9m5c5iY9NGdrTu6LdeSMtjfyHwySfEW1rAIGPMyCSydy+g5aPuoivyZEzaGKjWvlYz43F8JgOukIvilGPjYG/0dKd9jYs4b5S+wbenfjuxrkscSRICGShlJKezieS49ls81LRdkc7a3lbJhDE9HSQJWyjUHXE1SNEwpGpCiSVux6ho9WwGKp4AmIuKCO/p/jkzHZS2yzZjBtapJxHevgMAQ1oaxry8Q/bpPGcervJy/Ks+JOXiiwGIlHVGnowZM2DbvgjoYxEdnc+OJ7c+yYKdC0i3pvPY2Y8xPWf68TZJ5zPA976WsssxZw6y3X6crdH5InNijPI/B1S5gtzz2vbjbYaOzhHxlVDboMST5LoK/vJ+2REd86LKT5jRUsqvT735iPoBWLpsc4/lxtIqnlpVfsT9DpbrS1b0u+2M/3uQC6/404D7+nlrU7/iyVsbqqh1ajfBj7WGIX8QRuocM+rdYVp8QXLoO6fqtlo3uYrMSUfxJzaopwEbLE8BXwUuB3ySJHXlBfcIIUKd6TC+CiwBXGh5xh8DVgshdnS2XY7mmPiPJEk/Rsst/jDwlBAi8tmdio7O55u2oDar3x41YBk3NrHeOe9s3G++QcqXtdT+jowMbHWaE7kp0OeE6hOKj+s+JqbGWFyxGINk4Nen/xpZOv5B/V2zbo2qEQMGlFYFMmFf+z5UoQ7JRk/EQ3tYi7q8aORFbGzayN72vX22jdXX4/r733usizd0ixUGZ3fNk3K3NoYbnToadiwDIDMeo9JkoDXY96S1o0GXeCIJCSEJ3i5/m9tOui1RYyVRLF7RfntdpOEhiWRVS4k11MiTiNotnkhGI4aMDCzhSCLyZDCiYUyNEUOLfDLHHZg6xZNIfOA/TwWP/ZmWv/wF39L3MI8aheEAYQtAkiRy7r2X6htv0uyeNOmwdWiS5s3DteAf+FevRsRiSCZTd+TJ/5h4gj4W0dH5THhp70ss2LkAgPZwO7csu4Wfnfozrhl3zXG2TOdY43u/M2XXeXrKLp1jiy6eDJBkq5Gzxmb1u72/YWR/48v+2/e95VDD1P7HsP30NUibDr3PII9xiIP019cgVx9yUH8836f+z+Povk8SkvbcR8PxZYOfC3/DqcP6XD/Qz8RXF/4IgB9lemkZM6Wfffrp6+CDLOy5OKdpNzfPGTFomw7fvj97tOdJPgccYgLnbWd1z5Q83L/nxMqafvt5oH0dmy+5R1vYs6n/A+p8pozPdTKutv+c4hdNziW+8fCpvQZDilUvfjdIvtP5/OFB678BPAtEgfOAuwEHUAu8geaQAEAIoUiSdAnwNNrMzwDwHPDAsTNbR+eLR3tI+z50RGRMo7pj9kwFBRS/+WZi2ZGTk3AiN/gaPlsjh0BXDRCAd8rfYW7hXL404kvH0SKNjkhnvRNFy/1s9BkxZ5sJxoPU+moZnjz8ULv3SVfUSYY5g8kpkwFNjFFUBYNs6NE23q6934aMDIr+72kAfMtX4FqwAMlsxpjT/RnoEgvyk/LBXQtAZqdg0RoavHgihOD9mvcZkzqGESkj+m3X7NMiPLJD2bTYWqj11VLtrU7s0yWeOFUVD0kosgWv6iRd0VKPdQlJgyXaKXZYZU3oMGZmYg2HsSnaPeZg0nYFooHEa2vMgVHV+uyq1TIQzMOHU/jYY8TuvRfZ4eizjX3mTJLOPRf/ypXYTp522D5tU6diSEtD6egguGUr5sICFJcLJInLN32LW7mDr0y+acA2fs7RxyI6OseY5VXLeWTDIwCMd4/Hb/RTl1THrz/9NXvb9/KzU36GyaDfR30RidbVa1GtskzSvLOPtzmfSxRVYXXdat7c/yY59hzunXUvFsOxrR3yeUUXTwbImBwnz99yyvE2Q0fniKh/9yMGO1fu4Ssmg6IgGYf2dbH3Pu35mkI/2ZdPHlIfib5+3Hvdg5f1X7jyWNGyLxPXyv63/+yigcf3bHqhfzmsaPcGzr9wPCIWY+HTg7FQ51giDiGcAJw6PJ21R1k8SbLqP9eDQQhxSC1bCFEL9J2TsGe7auCio2WXjs7/Il2REElhCWNObr/tzOkZOCOag6PJf+JHnnQJCtn2bFqCLezr2HdiiCed19vcGYkgIzPMNoz9gf2UtJcckXhi8BhY+fJqbFk2QvEQVd4qRqX2rGutuN0AGLOysE3RJs3Ypkwh9ZqvIMLhROSJoioJoSfDkg4eTTzJ7hRPhpK67Z3yd7h/7f0U2AtYcvWSfqNsusQTR9xBZjiTVlsrH9d/nBBPuiJLnKqK25DE5Py1+Osc5HTa1h5uRwhx2CiMg4kRB8Ama+ldjZmZWJube9Q8GWi/vpgm8BhUAwZhwaRofUbVwaf5NOUfOrQ5/5Hf4V26NJGG61BIBgNJZ5+N5623aH38cQxpWk2jxuF2GiU/r27+2/+MeKKPRXR0ji2bmjZx3+r7EAhGekdyXeF11NTWsKF9A7vSdvF66evs79jPn8/+M1n2/idC63w+8a/UUnbZZ8zQUmHqDBh32M2b+9/klZJXaAh0T1gqd5fz+DmPk2xOPsTe/5sc/9hyHR2dE5qSCRMpmTwFNTr4m7FoXXdNxGBoIGl+//dwbO6/hqPovOYiduIVpNXpnyGUTdLR0dH5wuKJegBwhsCUk91vO0NaKilBTTyp89cOqQbdZ4Uq1ISgcEaBVqC00d94qF0+M7rEE4tqQZa1W71sSbvu+9r3DanPSq92rs6ok1Z3A8UOLcJ2j6t3yYUu8aSrlk0X5qKiHmmb3BE3qlCRkEhTBcS0iQk58aGJJ1ElymPrHwOgPljP+ob1/bZtDbgAsMbs5AY1QW9NXXeB80TaLlWF1AApI/cj2yOkq5ptMTU2pNRd0U7xxG46QDwJhxM1T0LxEK6wa0B9BWJa5IlJNWG32TGq2kzRiHr0MzkZnE7Srrmm3+iUg8m8/dvITiehLVvwr1wJRiMvz9OuXa3qP6H/t3V0dD4flHaUcufKO4mJGPmBfK7LvI4rr7ySW75xC6cZTuP05tMxqSa2tW7jukXXsbN15/E2Weco41uhiSfO8849zpZ8ftjt2s0v1v6C814/j8c2P0ZDoIEUSwrXjrsWh8nBpuZNfH3p1z8X6XM/a3TxREdHZ0BEywdfW6T1+WcSr8URlmyI1tYeWQdHEcXj+UyPpyp6vYvPE5+8sf94m6Cjo6NzwuCLdc7iD4geKZsORjabyfZbkISET/EPKoXRoaj2VvPMjmcSzuajQYO/gbASxiybmZkzE4DGwAkinhyQtmv4cC3KxBrUnPUHzi4cDJXuTvEkpkWNmF1aUda+itArHW6gt3hyMF0iQaollZ2rlyTWZ8c1gWGw7/9z25/DFe8WHl7Y8UK/bbvSbiVFMsgLFQCwsWkjwVjPmiZOVUW1a/YohhAWAY7OYIKhpO6KSZ2RJ0ZNLDFmZWENhzEIA5lKJgBLK5cOqK8ugceoGknNdGKKa+JJVAx+stPRxjx8OPm//31iOemm61mfo00ECshQ0/HZ1yvU0dH54tAUaOL25bcTiAfICGdwpflKvnL1V5BlmZSUFL7xjW8wJWkK8+rnkRJPoSXUwtff+zpvlb11vE3XOUq0P/8fgps2gSSRdK5e7+RQRJUoiyoWccOSG7hu0XUs3L+QiBJhQvoEHprzEO9f/T73z76fZy94lkxbJvvd+7lxyY3s79B9Ggeiiyc6OjoDIu4a/E2i97/ducwDb28c8rGFolB+/vFPhdGF+5VXPtPjRQIdn+nxdHR0dHR0jhb+uFYnIjVuQrbZDtk2SZUSDvqhRkkczBObn+DJrU/y6KZHj0p/0F3vZHjKcAqdhcCJI564w25AS9s1orMAuOpVAYY8k7C0rQzQIk8ADJ1Dwr6KxndHnhy6zp4rpAkdToOT0o3a7FFhdiZSY7UMQjxRVIV/7PwnAMVeLSpmbcvaRBTOwXjj2iQYWzSFdF8h9pidmIixoWmDtv0A8SRq0W6XVYfm/E9TRA/7B0NU1vpIsmjvizFLizwBGOkbCcAbpW8MKDLDG9ZsNKkmMnJSE5EnXUXkjzfOc+aR9/CvSb3uWjadlY04IBXZurIVx9EyHR2dzzOeiIfblt9Ga7gVZ9TJRdGLuOn6mzCZuuuaOJ1Obr75ZsZkjmFu3VwKw4XE1BgPfPIAv1v/O2LqifE9qTM03G8tpPm3vwUg83t3Yi4sOM4W9U1EiVDhqWBz8+YhjRmOlKZAE09ufZLzXz+fn675KTtad2CUjVxcfDEvXPQCr1zyCleOuRKrUZtgMz59PC9c9AIjkkfQHGzma+99jc3Nmz9zu09UdPFkECiRIIG63jcJOjqfF5SKoRdgrf3O7f1u861axf5zz+sdkRHtjpgwlNWhhkJDOrYYQsqw44k4ypEi8bbB5/3W0dHR0dE5EQiizebPlOyHbWuVDaRGU4G+oxqGws56LVXHG6VvUO2tPip9Vrg18aRYspMnd9arCDSjqMc/UrQrIsKiWjD9WUtjJbyaM34o4klMidEU1oShnPgIjIqDlJiWC3uvay+qUHu279AcBJvDZYfstyvyRA7LpKBFUfgyTyanU5xoCbYOOL3T7qbdBAlgUA3MqbqM1EgqCgqPbnqUuBrv1d4vNEHPHk3GHE0nN6Sl7uoSTw5M2xUxa7fL0XTtvc2Ix3rYP1BUoRIwakJJkV2LwOpK2wWQ587DarBS7ilne+v2w/bXEdSEIZMwkZmbjFnVPocq6gnjGEy9+mryHnyQ9Q0f9li/t2HT8TFIR0fnc004HubOlXdS6a3EFrdxvvd8vnXDt3D0kVLQ4XDw9a9/nRH5Izil8RSmeLUaXC+VvMRty28bUvSgzvHHu2IFjT//OQDpX/8amd/5znGzJa7GqffXs6FxA2+VvcWTW5/kvjX3cdOSmzjn1XOY+cJMLl94OTe/dzNnv3o2579+Pnd9cBfP7HiGtfX9T/A4EoQQbGzayA8//CEXvHEBz+x4hvZwO9n2bO6cdicrrl7BI2c+wtSsqX3WVytIKuA/F/6HaVnT8EV93Lb8NpZXLT/qdp4oDCaNqF6BdhCUTp0BQO4rT5I2VQ8N0/l80bpxMYGnFw69g1jvm08AEY9T9507AKi97weMePpf/XbR/tzzZN7+7cEf+gS5CRwovmXLSL7o6NV1bH/0SaD4qPWno6Ojo6PzWRGWNOdwljXtsG2tJiMpkRRIgn0dRx55IoSgLd4GkuZU/uvWv/LHuX884n67Ik9GlX9EVnUJhmQDcRGnNdRKriP3iPs/Epr8mkBiiVtIaW/HJknY45pw1RJsQRVqv4XU+6LOX4eKikE1MDZ3Aj6fj6jXh0EY8Mf81PvqKUouSrRvbizHCqzxbaOgZSsnZ5/cZ79dszAVr0Jqp8DWHHcyIrkIScSIqTE6Ih2kWw9fBHbZDi1yJTOcxYj0yUxon8y63I95u/xtOiId/GXeXzDJ3bOSg2gp3OyxFMyRNFIjqQCUukoB8Ea6I0/82EFViXbWTs1SYoBp0I63Rk8jQhIgYHiKVqDdkJmJKRZDVlVMsol5+fNYWruUX637FReNvIibJt6UmBF6MB2dUckmxYwj1YrD2O08DMVDmMymPvc7HpT5SkGC4bE41SYjtT49bZeOjs7gUFSFn6z+Cdtat2FSTMxtm8u3b/o26Z2Fwv2rV9P4wC+xnzKL3AcewJCUhM1m46abbuKll15CqpFIiaawOWczm5o3cd2i63h83uNMyJhwnM9MZ6AEPvmEhh/eA6pKype/TPZPftKnAHC0EELgCruo89VR76/vfvjqqfPX0RxoJi769pF1YTfaSbOm0eBvoCnQRFOgiQ9qP0hsz3fkMylzEhMzJjIxYyKTMiaRYjl05G5fBGNBFlUs4uWSl9nv7k63NSt3FtePv56zi87uMQ7qQlEUSkpK2Lx5Mw6Hg/nz55OalMqCLy3gx6t/zKraVfzoox/xk9BPuGHCDYO260SmLdTGXYu+OeD2ungyBNo/fEsXT3Q+d7Td9KNj0m+srTtNRWDvocP61PDQIk/6mjV4IqOGexbr3DteG5SNXv0Rpuz+i+X2hRCCWGUVJOviiY6Ojo7O54tIPEJM1n7Dc5xZh21vN5uPauSJO+ImJnVOwBDwXtV73DPzniMWOLrEk5GxOAZ3GTnOUTSg0BRoOu7iSb2vHoC0oBFZCJLa2wmkpSAhEVNjtIfbybRlDri/6g4tWscRdzB56nj276uiwVtKWiydNnMre9r39BBPXE2VFAA+G/x9+9/5v/P/r89+uyI3LIqFdLkFVKj2qIweMZ704HZcRgPNgeYBiSebmzaDBAWxERRPy6bqw5MRcpxNOZtYXbealdUruWDkBYDmYIh3fiaH5xQRKLOSFtGuR1equETkiaLSEsonzdtGPCVEDAPpndHFg03BUdmq1Y2xxa04kjUh0ZiVhQRYIxGCNhvzc+fzXu177Hfv54mtT1Drq+Wh0x/qsz93yA2ASbFgd5qxWe1IQkJIgnA8TLI5eVD2HSsi8TCVBAGJU0zFVFNDQ1xPR6ujozNwhBD8dv1v+aD2A2RVZk7LHG676jby8zUh2v3mWzT+4hegKHjfeZfw9h0UPPE41nHjsFqt3Hjjjfz3v/+FCpgbm8v2kdtpDDTytaVf48E5D3Jx8cXH+Qx1Dkdo2zZq7/weIhbDef755D30KyT56CRS8kV9lLvLKXOXUe4up9ZXS71PE0rCSviQ+5pkE/lJ+RQkFXQ/nAUUJhVSkFRAqiUVSZIIxALsde1lj2sPu1272ePaQ5W3ioZAAw2BBlZUd6ezLEgqYFLGpISoMiF9Qr+CSpWnilf2vcLC/Qvxx7SoWpvRxqXFl3Ld+OsYkzamz/2CwSCbN29m48aNeL3exPry8nIuvvhiJk2axGNnP8Zv1/+WV0tf5ZENj9ASbOGu6XcNagLOicqqiuXcv+Y+OkKHfn8PRBdPdHR0johYrPvLVhymKnwsemKEx1bcegORNVso+s+/SJp12jE9lntpdxHU/WfNZUJJd+o/dQDpyEJbtqCE/HBi3APr6Ojo6OgMmBaflnZSEhLZGYfPSW2z2UmJammgan21+KN+ksxJQz5+uUub4W6L27AoFtwWN7vadh2RwCGE6E7bFdWEmbyQjwablcZAI9OYNuS+jxRFVWgJa9c806vd3Drb22lNSyPZkIxH8dAcaB6UeLKrWhu3OGJJTDi5mFAgzPZySA6n0GZupaS9hPkj5gNaLvpohzbW89tga8NadrbuZErWlF79dokPVsVKTqAJbLDNksc0i0SObzMuo4GWYMuAZgVXKRVghElJUykcl4ZtcSEF9kY63B3sS93H8urlCfGk67iyKjN+0kj2NLjI8A0HwB1z0xHuwNeZSiNZVakJO8kzKPhTwwRlMxmK9vkcbORJdbsmQiVFzRhSNCeIMUsTFC3BEEGbjUJDIW9f8Taralfx2ObHeKf8HW496VaKnEW9+vOEtVS5ZsWCLdmMzWrDIAzEpTjh+MCdAcea9ftXEpMkUhWFubPu4LUt99EoK4RjweNtmo6OzueEZ3Y8w6ulr4KAU1pP4Zvzv8mYMWO0yIC//53WvzwOgPP88wjt2k20upqqa64l94EHSL3qy5jNZq6//npee+01SktLObXsVKonV7PVs5X71txHSXsJd02/C6Osu0dPRML7Sqn59u2IYBDHnDnkP/onJOPg36tQPESFu4L97v3sd++nzF3G/o79NB+ixpqERLY9m4KkAgqdhT1EkkJnIVm2LAyy4bDHdpgczMydyczcmYl1vqiPkvYSdrftTogqNb6aRITL8urudFlFziJNUMnQBJVgPMh/S/7L2oa1iTbDk4dz3bjruGz0Zf1OoGhubmb9+vXs2LGDeFybSGK32zn55JPZv38/zc3NvPbaa+zdu5eLLrqI+2ffT44jhye3Psm/dv2LlmALD815CJPhxIluHQzheJiHVv6Id5s+AqA4GmWghTn0bwcdHZ0jwvNcd/F0Q/OhxROPZx9DKeelBgJD2Kt/Imu2AFDz+x8z8fU1R7Xvg2n8wT39blPCvsPuL2Jx1Ih+g6mjo6Oj8/mjyaOlkDIrZhy5eYdtb09KwuKOkRS34TeGKGkvYWrW1CHfpO1r0iIJHDE7SXEnboubbU3bOG/40CPI20Jt+GI+ZCEYEYtB4SnkRTSRpsE/9NpyR4PWUCtxEUcSEhmdReKTO2cUJqlJePDQFGxiEpMG3Gd5qyYUJcdTMZoMDB9dAB9BSmfx+L2u7tvOZVXLyA1p+aMdIhdo4YW9L/D7rN/36rct1AZokScOgzbOWzT2TEy+3WTHFfZYOKRDo4taTy0Box9JSJw97iyyRyRjMdqxBfMosLSzL3Ufa+rWEIwFsZvstPg1ccmqWMnMTmPEVImOrek4Yg4CpgBlHWV4I24AbJJA9Zqx2fLw00jUKJMxxMiTuo4a7TqGjZg6i9vKDgeS1Zqoe+L3+5mRMoORKSPZ0LiBtQ1r+cfOf/CrOb/q1V9XajGTasGebMZmt2BUjcTlOKH40CK9jwVbqlYDMEwxMXv8eaRsVPEYZNaVrzrOluno6HweeLPsTf667a8ATHVN5YZTbuDkk09GKArNv/kNHS+9DEDGrd8i64c/RHG7afjxTwisWUPjz39OcNMmch/4BSabjWuuuYY333yTPXv2MGrHKIafOpyFTQt5dvez7Gvfxx/n/nFIKZN0Dk9MiVHrr8VutOMwObAb7QMSHaLV1dR865uoHg+2adMo/OuTyGbzYY9V6a1kf8f+hFCy372fOl8dgr5rXOTYcxidOppRqaMYnjxcixxxFpDnyMNsOPTx+kNRFFpaWnC5XOTm5pKRkdEjzZjT7GRW7ixm5c5KrPNGvex17WW3a3dCVKnz11Hrq6XWV8t7Ve/1OIaExNzCuVw//npm58/uMypEVVX27dvH+vXrqaqqSqzPzc1l9uzZTJo0CZPJxLx581i9ejVr1qxh165dVFVVcemll3LbSbeRbc/mwU8eZFHFIlwhF4/NewyHqXetoROZvS07uXvZbTSoWoTOlf44MyY/yGJuGtD+uniio6NzRHjefXfAbWM7Gg/fqA86/vzEkPY7HOphwjCPNdEBiCIiFkU+cSYQ6ujo6OjoDJiKds3x7ohZMOXmHLa9PSUZ3B2khZPxJ4W4dfmtmAwmXrzoxX5TDwzk+Ol+I2kRG1VO2Nm8c9D9HEi5RxNKiuJxzLIRJlxC3qZHAWgMDG2cc7So92spu+xxO/ZQBNuMGSQ3aOssMQsY+y4arwqVHa07sBgsvSI9GgLa/ulo0SpZBWnIqjlRJ2Rv+16EEEiSxOKKxdzd6bdPU4cBLWxs2pjYfiCtgVYAkuIyRnNntJEll1UxHzM7BYqBiCcrdq4EIDWSytSTJ2AwyuSPTiVaMowMZ7MmihBgdf1qLhhxAfUdnddDsZCS4aB4qpGdG5NIjiZr4om7LJG2y2oAySXjGD6SVrYQtUJ6vFM8GWTB+IZO8SQ1ZMKQql07SZK0ovGREFexhMKPV8HkxWBJ4vapt7O2YS1v73+b20+6nbyknuKjN+TrPA8bhopPmdH0a0zFEmEgED26k46OhMqOPQBkmzOxmCwUK0a2GlQe3PzwcbZMR0fnROej2o/41TpNPB7nHsc1Y65h7ty5qJEIDT+6F9+KFSBJ5PzsZ6TfdCMAxrQ0iv7+f7ieeYbWJ57E89ZbhHfvpuDxv2AZOZKrrroKo9HIjh07MH5q5M65d/LP+n+yrnGdVgflnMcZmzb2eJ72F4aYGmND4wbeq3qPlTUrE7+tXdiMNpJMSThMDu3Z7EgsO0wOMnxwyq/extrqJTIyj+Zf3EirdzeOUHc7X9TXI4qk3F1Otbe631ok6dZ0RqeOTgglY9LGMCp11FFJdRkMBqmrq6O2tpa6ujrq6uqIxbpr9zqdToqLiykuLmbkyJEkJ/c+ZrI5mVPzTuXUvFMT6zwRTyLV1x7XHna37SaqRrm0+FKuGXcNhc7CPu0JhUJs3bqVDRs24Ha7AW3cMWHCBE499VSGDRvWY2xmNBo555xzGDt2LAsXLqStrY2XX36ZadOmccEFF5B5biY//PCHrGtcxzfe+wZ/O+9vg4pkPl6oQuVv6/7AP0tfJC5BZlzhOoq55IZ/45QtA+5HF0+GQPTpD+Cu421FN4FPP6Xm5m9QvGQxluKh10VoefTPuBYsYNT7KzAX9v0PqKPTC09Pz76Ix/sNozSXtQ7tELu29ftlFW9vp2zO6QA9UmKdqETr6gb1/1V7623H0BqdzwtDrReko6OjczzZ06I5TrP8Vow5hxdP0jMzobqalEgGtUlaIc54PM6CHQv4w9w/9LvfypqV/OjDH/HQ6Q9x6ahLE+trvbUAZPoMFHpl1hdCmbesT2f+QOlK2TUyGoPMsZA9kbzO1AcnknhiC4VImj+f5H/9CwBD0ADJ0BzoKUh80vAJD617iHp/PSbZxOIrF/dw1LfGW8AIuRYtt7wsS1hlJymxEDIy7eF2moPNZFgz2NO4HWunn8AqZSMLmdZQK3X+ul6pp7oiN8YG20CGVkMaAaOd/fZhXNwpULT4D38911Z9AkButAiLXYtQKhiXRs2edtLM+RQGCrXUXVXLuWDEBTR7tfO3xu3Yk82k5zmwSE5Soik0OhrZ27IXb1yb3GI2gq05RlLKJBbuD/Gl2C4K1N3A4NN2tYZawACZcWvisyeEoDF/DnkZZUxhH3QA790Hl/+VadnTmJEzg83Nm1levZyvT/p6j/780c7c5tipefd+Rpu3kyHG4APqvHVMz50+KPuOFQ3hJpChIFlzRl468iZi5QvYLh1+xrGOjs7/Lttbt3PPh/egCpXhvuFckXEFF198MarXS+13v0to02Ykk4n8P/6B5Asu6LGvJMtk3n47tmnTqL/nR0RKS6m66mryfvMwyRdeyBVXXIHRaGTLli00ftjIfefexzMtz1Dnr+PGJTfymzN+w/nDzz9OZ/75Jq7G2dS8ifcqNcHE3RnJCZpYElNiCWEjFA8RiodoDfX2ETmDgl+9oGB1QWMaPHBpC55N9w3YDqfJyeg0TSAZnTqaMamaSJJhyzjicwQtmqOtrY3a2trEw+XqPanCYrGQkZFBc3MzPp+P7du3s337dgAyMzMTYsqIESOwWq19HivFksKc/DnMyZ8zINtaW1tZv34927dvT4g3NpuNGTNmMHPmTFI7J3D0R2FhId/+9rf54IMPWLduHdu2baOiooLLL7+cf8//N3esvIO97Xu5ccmNPH3e04xMGTkgu44Hzf5G7nr36+yONoIEZwSjXDDuLi6d9x1kSepR7+Vw6OLJF4Cam78BQMVFFzN+x3akw4Sx9YdrwQIAmh95hKK//vWI7TqSG1OdwVHx5PcJ/3MlUlgl54FfkP7Vrx43W3zb15E848yj2meHv5X+ysxW/qN3KoOBIjcem5AOf/k+UvvZVn7e+Z8LkUfnxKJ641r41snH2wwdHR2dQbHfXQZAvksemHiSn4/x008Z7RvLZedcgTPJwU/X/pxl1cv4nu97fdZ+APj3zn8TF3Ge3/18D/GkMaiJCTluwcimONJUCZ/ioyXYQo7j8Pb0RVex+FGxGBROhvRi8jqd/Y0DcPb3RWlHKU9seYKvTfwap+SdMqQ+oFs8ccQd2INBzMOKSBs+jInKPjJieyjDRFOwZ+TJHz/5I/Wd0SUxNcby8uV8fWq3o94juwEYfsDNsdORSjDgIkPNpFVuYa9rL9mObGxBzSGiShKQSmoklXZrO1tbtvZ471Sh4o5q/U6N1YMF3s/UnAJtplRS0ESQFk/1Ic83GAuyPbYFZJhgOimxvmCcVpBdaXdQmKqJJ6tqVrGrbReNnankrHE7tmQzBoPMiEnZpHZosye3tWxD6UzrYTaBsz5Eo3U871ZkkmwwcqttBzD4tF3tihsMkCOl0FTpobnCS21JO7X2OVyf/Hx3w63/gdHnwqQrOX/4+Wxu3swHNR/0Ek8Ciibw2CUH6apWjD5fUagCqg9z3T4rhBDUEQIkxubPBuAr5/2I0SPmsfqd73L3cbVOR0fnRKXSU8l33/8uETVCTjCHi80Xc80116C2tFB7221EyvYjO50U/vWvOE7t/zfTMXs2I996k4Yf3kNw0ybqf/BDgpu3kPPje7n00ksxmUxa/YeVO7jnvHt4xfkK6xvX88MPf8itU27lzpPv/EIUxz7WKKrClpYtLKtaxorqFT0mF6Rb0zl/+PnMHzGf6dnTkSWZqBolEAsQiAbwx/z4Y35tufMR8rgY9+DLpLhaCaTZWHXPKUxIVgjEAr3a2ow2ilOKNYEkbUwioiTHnnNUfZHhcDgRTdIVWRKJRHq1y8jIoKioiKKiIgoLC8nKykKWZWKxGDU1NVRUVFBZWUlDQwNtbW20tbWxYcMGJEkiPz8/IaYUFRVhHERdF1VVKSsrY/369VRUVCTWZ2dnc+qpp3LSSSdhMg08Ba7JZGL+/PmMHz+ehQsX0tHRwX/+8x9mzpzJv879F99f/X1qfDV8benX+Ou5f2Vq1tQB9/1ZsXDXSzyy6RECksCmqlwTTePKK55nVN7QAg508eQLhmfJElKvuGLQ+6nhbieyCPf+EhgsuydPQI6D7Q/3MOKybx1xfzqHJvLUCrp+Gpof+vVxFU/aX3r+qIsnWS39fybj/1re77bDIbnj7B0/gew/PEjGZdcOuZ+D8f3zObj3PtpfePGQ7Zq/f+9RO6bOF5to7Mi/l3V0dHQ+a2rDdSDByDYSqYoOhXX0aJK9XtozMpgcLWbKxr+wKBxlrdXMc7uf4/7Z9/fap8HfwPY2bRZfSUcJdb66RAqDtrgLZCgMWsgxWHDGnHjNXva27z1i8aQ4FofcKZA6jDxFc7Y3dooXXbSF2qj2VjM9e/ohb+Kf+vQpPmr5iE/qP+HJc5/k9ILTh2Rbva9TPIk5yApXYDHUkzlRcLW6lOWKDcjsEXniiXgo95eDBMXeYiqSK3qIJ76oj6is/f6MLxif2C8jI5PmQDmpkXRabS2UtJfQHGjG2RUk6XBij+WRGc6k3drOluYtXDbqsh7HVdFSdZ0kazYvyTpD2yhJRA0ZQJjmPlKMHciLW18kIkdwxBxcPumKxPqsoiTMVgNKwEmKPYWCQAH1jnp+9NGPyFO0CBq76sBg0JxiwydnkL5Mi7apCWrptUxCoBrMpLZ7WNisRUk0ivREzZNgPEgoHsJmtB36TenEK2mptLItObz1xy2oqvaZOcm+lFSpnUZzJm9nzeP2+tcQS+9DGnsh5xSdwyMbHmFry1ZcIVePGbNhNQgypBsipCvazMmxUT+f2KyJiKvjTXnLXvyyhFEIThk7P7H+5NEzKPrGUu6+J/04Wqejo3Mi0hps5fYVt+OJekiLpHFB9AJu+uZNqFVV1N56G/HmZozZ2RQtWIB13OHTa5mysxn27L9pffwJXAsW0PHCC4R27KDwsT9zwQUXYDKZ+Pjjj1n7/lpumHcD4yeO57k9z7Fg5wL2dezjkTMfwWl2fgZn/vmiK93ne1XvsbxqeY/okRRLCucNO4/5I+YzK3cWRtmIqqqEQiHMZjMWkwWLwUK6tfdvgBoOU3vrbQQrWjGkpTHlxReY2U92HVVo44ijLXAJIXC5XAmRpLa2lpaWll7tTCYTBQUFPcQSu93ebZ+i0lLlo6MpSOH4NEaNGsWoUaMALcVXVVVVQkxxuVzU19dTX1/PmjVrMBqNDBs2LCGm5ObmIsu9zzMcDrNt2zbWr19PR0cHoKXmGjduHKeeeiojRow4IhFp+PDhfOc732HFihVs3LiRTZs2UV5ezm8v+i2P7HuEXa5dfGvZt/jDWX9g3rB5Qz7O0SQYC3Lfom+xyrsTJBgfiXFF3jVcc9GDmAxD/6zo4snnHMXXM2+gGh2ag635z48mXge8R17sUu5MMRj68aNwgogn7o3v0/Dtuxn28vMkjTsxQtmPFccq6ie8bx/WceMSy/HW3iGWocUfw6O9Vn8mNLz9d/Iu09Jc9Xf+arB3nZGWHx9d8aSL5of7zucca27BlJNNZOv2o35MHR0dHR2dz4pGfyN7XHs4u+jsXoU/Q/EQHWg3chMCDiRJoqnCw67V9bQ3BMgtTuGs63o6PgwpKaTF4rQDxvXPgGsJ37BaWJuXw8L9C/neyd/rVcx1ScWSHsvLK5dzy0m3EFEi+Dsd1qOkVDJzs0mLePCavexu283ZRWcP6Zy70nYVR2OQOxkMJvIceYCKPx7EE/GQYklBCMEd73emNphwI/fOurffG/zNLZsBiIkY31v5PX5yyk+4Ztw1gx7L1Xg0x39SzMK0Uyowr/0hFgAJcjtTix1Y8+TDyg8RkiA5msyFORfxVOiv7PbtThRXr3RpEQ1mxczokSMS++Xl51Bf4yU3KFFmgz2uPVhUK87OYvHmzAyKR4ym1K85+7c0b+lhZ1fUhkUxkmYKoRgsrEmdQb6rBXdSMj5TLlBFS2d0yoEoqsKTW58kokRYvGcJSDDBPY2pp3XXxJENMvlj06jaoeCwOJneNp1oepR6fz31aGJNkujONV40IZ20N/ORhISQtHO42usnaLVhjcZYuFebRVsh8kgSApMQxCSJ9nA7BUkFh31fVKESMGrKUoqpGL8qsCWbGTsrh2Hl6yAMTxZ+lZfyLuGSto8o9DfBlufIO/XbTMyYyB7XHj6s/ZCrxl6V6DMstHu+NLnboTMu4ges1PnrDmvTZ8H6Mm2CU2EcctNye2wzG/S0XTo6Oj3xR/3c/v7tNAQacMQcnOc5j2/c8g3kvXup/u6dqF4v5lGjGLbgGUz5+QPuVzIayb7nh9imn0zDfT8lvGMHFV++ivzfP8K5556LyWRi1apVfLTqI84880zGnTGOX637FavrVnP94uu5pPgSxqSNYWzaWAqSCo57NIqiKlT7qintKKW0vZSyjjJkSSY/KZ9CZyH5jnzyk/IpSCogyZx01I4rhGBX2y5NMKle3mM84TQ7OXfYucwfMZ9T804lGopSX1/P6g9XU1dXR319fSJSw2AwYLVaezwsFgtWk4nCF17Etns3wmYj/JMfUx2PY6mu7tHWbDYjSVKv90EIgaIoRKNRYrFYj+eBrotEIjQ1NREK9U6ZnZaWRmFhYUIsyc7OxnDAb5kQAleDn7qSDupKOmgo7SAa1iZcSLLE6OlZTD13GDkjk7Hb7UycOJGJEycC4PF4EkJKRUUFfr+fioqKRBSJ1Wpl5MiRCTFFCMGGDRvYtm0b0Wg00Wb69OnMmjWLtLS0o/a+m81mLr74YsaPH8/bb79NR0cHb734Ftefej1L85fyccPH3P3h3dw/+36+MvYrR+24Q2Fjzcf89IO7aJaiSEJwedjM1V96lqnFM464b108Oc4IIYi3tGLKyR7S/vV/+EWP5Y4t75F+zeCdwO7nX+he2FHRf8PjgBCCkgnal8rYT9cNaOZiXzTe9D0koPqmm5i0YffRM/AERESjSJbu4kfesvVHpd/Ky6/okXKq7MyzBt1HvKMD41H8Mj+Q9j8/je/lNxD+EOMWruqz9sr+71zT577epUtJvvDCwx4jvPfIU25V/fj7jHnuv0fcj46Ojo6OzvGiwd/ANe9cgyfmYf6w+fxu7u8wyd0pAfa27AVJK8w9KjkXVVFZtmAX/g7t5rm1xseMC4fjSOlZrDHPacbJbsa4PgBgakhldDTKfjMsqVzC9eOv79H+ndJ3AK1guNviZlHpIm456RZq3DUggVE1UpSSS3LxKNICTVQ7YVfLriGdsyfiSRQKHxmLQc4UAOzpoyiM7KHOZOK10tf41pRvsal5E3vbtTHDC3tfIBQP8eCcB3v1WeutxYMHSUjkBnNpdDTy8PqH2d66nd+c8ZtBCSh1Ps1pPiXowmyLERdmJFsKVfVmcrK1iJOWYDOKqmCQDby//30Acv2FREtysE+wEzQF+bThU84Zfg47q7SaNY5YEll5qYnjjE73M4v/sCcss4Zs1jetxy4cjO70NZjS05g6eyyb3tGieyq9lbSH2xOzTLuuYarmU6Ay73TCBgtFHT6ckRAu2wigCp8aTQg5XbxR+gb/3PVPbUECk2Li8vxrMRh7OlEKxqZStaMNGxkEVT83OG/gXeu7VLorkYXMCLVbbHGmW0lLyiY9ko7L6uKGsODH7R1szB7GjjGn4Q5pOcNrRA5RjGQoCk1GI66Qa0DiSbO3GVVSQYDdoM2gHTE5gzOuHk3gYS1KJBBwMKO+iieH3cDvyx4jsPw3bA4Uc2bumexx7WFlzcoe4klE0v6PCpSaxLqiToGsKw3b8WZfsyYK5sr6rG0dHZ1DE1Wi3L3qbko7SrEoFs5uPZtbbroF0+bN1PzoXkQ0iu3kkyl6+m9D9gc5581j5BtvUP+DHxDeuZO6279Dxq23ctZd38doNLJixQrWrFnD7NhsnrvgOe7+8G6qvdU8te2pRB92o53RaaMZmzaWsWljGZM6hjFpY3pN7DhaeKNeSttL2dexLyGW7HfvJ6wMLP14sjmZgqQC8pO6BZWu5YKkAhwmxyH3F0Kwt31vIsKk/oAIW4fJwTlF53Be0XkUG4ppbmim7tM6/lb3t0QURF8oikIgECAQCBx4IGZ/+im26hriBgOrT5tN67ZtsG1br/0lSdIEF7MFSZaJx7sFEFVVB3RdDofRaCQ/Pz8RUVJUVERSUm8hytcepq6kPSGYBL3RHtstDiPJGTZaa3yUbWqhbFMLucUpTD23iOJpmcidkRApKSmcfPLJnHzyyQghaG1tTYgplZWVhMNh9u7dy94+fFGZmZmceuqpTJ06FXM/JRzUaBSlrY1416O1jXhbK/G2NpQ2F/G2Nkx5uSRfdhlJZ5zRpx9t1KhR3HHHHSxbtoytW7eyZf0WxmeMxz7OzvLG5Ty07iFagi3cMfWOz7x8g6Iq/H7FvbzSuBxVksiNx7nKeSZf++qT2M0DLwp/KHTxZIC0fNgz/Y6qqn2GTQ2WLlGg8Km/4jz33EHv72/eyYEfy+jCT+GRIzbrqBJ2u7CmDr0wU8XFlyRel84+LeG8d3+ygsZbvo/xjImM+ccbA+5P9h6dL9QTGSUSQD5APKl76td8tl9foPQR4QHQ8uij5PcTkdEXkYqBi3mG5ghqs3YTWn7/LYx+5Pke29VIBGV9eZ/71v/gh4Tqysm59c5DHqPyyi8PyBbRmdahL+Lr9YgTHZ3/JZo6mkhOTj58w+OIoirIknzUBrt63bMjxxPxEIqHyHXkoqgKVd4qRqaMPCozHoOxIGaDGaM8tFuBYCzIbUtvwxPzALCsZhnRD6P8Zd5fEvZtrdsKQFooieTiUVRub8PfEcHmNGGyGPC2hWmu9FI8rbuqmfA2cIbjFaxoXviPlJN4STmXq30LeCQjnTdKXuW6cdclPlv7O/ZTGahEEhKzWmaxonAFZYEymgJNlDSVAOCI2UkpKMAxaSJ5yzeyLQu2tm0lqkQxGwZXJ7ArZVduPI41uYi7361GiezjGz47d0Q8/CwrkwU7FnDF6Cv41xatUHtaJI0OcwdvlL3BbSfdRn5Sz9myH5R90NkunavEdXzkep9d6bt4t+Jdzio8iwtG9iyE2x8xNUZbpA2AU0QrSLAzeCHhqb8g8sGdjM6IIgtBHIX2cDuZtkw2t2vO7SLPWORAEnnBfMpT9rOsbBnnDD+Hsqb9ADjjyYkbfLwN5K75NhJRTo7CGGGhLB4iRIiTO8UTQ1oa+RPTcb6WgzPqxGf2sbV5K+cO1+51uiJPshXNybA250zkphDby61kJwWpGTOSDP9KXEYDu9p2JerAuMNuHtv0GADp4XT8Jj+TXFM579bTel2PwvFddU/s4IBAeYA/X/JnXnvlTYIRH8PSehY4HTGqkNlVswkZQ3xffh0ZiATNfJiv5fG+ZEoOi3Y2U6YWkKGEaTIaB1w0vqK1c+aoYiEcTgXCZA1zonhqcSgBYpIBo0diYksJS+ddRn3NCxREWgmufpI6x0TIhnUN62gNtpJlz6I93E5M0q7dtLBWV6jZnE5RzA1AR6yDiBLBYjg6DoOhUu/Xaq/k2fquVaSjo6MDWnTe/R/fz/qm9RhVI2c0n8E3vvwN7B99RP3DvwEhSDrvXAr+9CfkfopqDxRzYQHDX3yBlj/8kY4XXsC1YAGhbds45dE/YTKZWLJkCZ9++inxeJz/XvRfFlcuZl/HPso6ytjv3k8wHmRH6w52tO7o0W+OPadbUOmMUhmRMqLHpJLDXYMabw2lHZ1CSadg0hjou5aa1WBNHGdM2hgkJBr8DTQEGqj319Pgb8AdceONevG2exOTOQ4mxZJCviO/h8BSmFSI0+zk4/qPWVa1jBpft0hvM9o4Ped0TrKeRKYvk+Z9zaz9cC2rldW9+s7MzKSwsJDCwkIKCgrIysoiHo8TDod7PkIhpAX/wFxdg5Blmr92ExnDR2D1BwkFQoTDYaKxCLF4FIFACEEoFOozOqQLWZYxm82YTCbMZnOP14dbl5mZSU5OTp81R8L+GHX7OrRHSTuelp42GE0yeWNSKRyXRuH4NDKLnMiyRGutj+0raynb2ExThYemCg/OdCsnnVPIhNPzsdi6jyVJEtnZ2WRnZzN79mwURaGhoSEhptTW1qIoCmPHjGHmxIkU2WwobS6CS5bgSwgjPR+qx9PvtVJkI57kYqSKMlKWfg9TZiopl15GyhWXYx3bM0LcarVy+eWXM2HCBN555x06XB041zmZP2U+y3zL+L/t/0dLsIVfzP7FkO8xBku1q4wfLL6ZMuEFSeLMMFw/5y+cOWX+4XceBLp4MkB8Wz7usVz51F2M+t6TR9Sn5913E6/rvnvnCVVEOt7ejjF9aHlolYOcxrGg94jEk+hBznM1EkG2WKh++MeYgfjHe4i7OzCmHptohr4IfPIJittN/Q/vAWD0Rx8NOXoIwLtsOfV33QVAzv33k37jDQPet3nZv3qti1RXYJrS/f5F6n0c2TCjG//atSSdfvhc3KXT+w6N8694HwYhnjS5h5Z6ILZwYy8hseK6q/pu3En7o0/1KZ6UX3Qx0YoKxm3ZPODjt/3t6QG31dHR+WLz1va3+MnwnxxvM/rFF/Vx45IbkZB45dJXjsjh1hHu4NpF1zIufRxPzHtCF1CGiBCCry3+GhW+Cs4ddi5VnirKPeXcdtJtfO/k7w25X0VV+N2G3/Fa6WuoQmVC+gSeveDZHjP7B8LTG5+mOliNJW5hUscktmVsY1XtKl7a+xI3TrwRgD0tWtRCjteCZewoPlml/Z5PPCOfSHuYfa4wzVU9xZPKdQspJkSrSOE/8fNZaL2corxsRtW9iTlNZZ9nP3tce5iUOQmAt8reAiA3mEte+1QyM7fSZmvj2R3PUtOu3exn+u1YhhdhGT+eUc+DdaSVAAE+rv+Yc4adM6jzPjBl18rwBBZu16I5Mg2p/MIU5KVsO7viQe764C52tmq5lmc1n8aWrA202dp4b/973DLtlh59rq1Zq10nfyGGhlFcPzebFyr+w560Pfz2099yRsEZ/abd8EQ8VHmrOCnzJJoDzQgEsiozA82h/rpyOsM+bWJuTg51IkSW0kqz0Uidv46OSAc+4cOgGhhvmM6oU/MoqRtDecp+Pm76GEVVErUz0kTnON5dg3j+CiRfA0GzCXs0xjdbG7gvW9ueFjACUQypKZitRnLSC8gOZeMz+/iw7sOEeNLo1ZxBeZ0zZ99yTse4Xavb0eq3USHlcWYoxEJnEqtqVyXEk8e3PI5f8ZMcTeb8yqswKVbGj5lMUmrvUW5GfhIWm4waSMGUYqK9vZ3nn9cm1ciKmcKcnuLJ6CmFfLo/CatqwSxrE4BiHQa22bTomdvmjuaDkjpKxHDSFe2ebaBF46saSwFIilhoa9Puk7KGOWmuXUM+UGEtIikQR5IFYxpqeGzY1/hT2aOcI61jT2AMhRRSJ+p4rfQ17ph2B2+WvgkSZEadjIjV4DPY2ZByJpe0vo1FlYjIgnpfPcWpQyuKejRQhUq10gEGGJ497bjZoaOjc+Lz6KZHWVq1FElIzG6ezQ3n3UDakqU0//3vAKRedy25v/gF0lFK9yebzeTe/3PsM6bT+PP7CW7cSOWXr2LSn/6E8bLLeOedd9i0aROxWIwbL78xMWk6psao8dZQ1lGmRYF0aCmzGgINNAebaQ42s6Z+TeI4RtlIcUpxD0FlbNpY7EZ7t0jSlXrLXUYo3rcYkOfIS+w7Ln0c49LGUeQs6pUu9WACsYAmqPi7BZWDxRVPxIMn4ulXXAEwy2Ym2SYxMjISW6ONcFmY6s6/Lmw2W0Ik6Xq22XrXBDMajVgsFixGO4ZoBDUcJv7s3zB88AECibozbqfedTLBSm2CgATYOh8CAZKKKsURUhwhxxGAJGQkYeh8dL5GBgmSM6yk5thJTbVrz7l20nLsOFItPe9R4hFw14KnFuJB8ITBmUsMK41lbi2yZF8HrbU+EN27SbJE9nAnRRPSKRyXRm5xCgZT70lOWUVOzrt5IqddOYpdH9Wz66N6fO1h1r6+nw2LKpkwJ4+T5hWRktX7msmyTK7BQEo4wgSXC19FJaGqKgyvvY6iKFQd8lNwACYTxsxMjJmZxDKKaEsaTTN5NAeTUFTNZlmNkeIpJ+39UtJev5usoiTSrryc5Isv6pE9ZuzYsdxxxx0sXbqUnTt3krQjibn5c1ljWcObZW/SGmzlT3P/NOj7i8Hy7Cd/4el9/yQog0NVucowjm/d+G/SHEc/EkwXT4ZI6JNNMPR7VwAa7v3xEdshVNEroiBcUoJ1/Pg+2w8UxeMZsnhS/sbjR3Tsw6G4Pcg52ahKLLGu9IaLmLh43TE9bhfhvXupueWbPda1/vnP5P++p6d+7/gJAIcVxTo+eo+mu36QWG5++OFBiSeuxa/2+gzUfuWmxHGbXvwr1p29C1wNldpvfuuw59TyeP+fAeUQqndfBP9z9NJbxfb2HXVyICIe7xWm2CXg7etHEOqLtqeeOuT2SN2JkY9aR0fn2LO6cTU/4QjEE3cNlC6DlCIYN7BZ6IckHoWqNdC4HaZex2+3PpmYUb+ofFGP1DADxtcEpe+xzL2bxkAjjYFG1tSv4azCwad37LZxNVSthYmXQ/60ofVzIJ46KFkCYQ+ccTd+JcKjmx9lXtG8odkpBLjKofpjalIL+Hvjh3x5zJeZkXMEeXVjISj/gJ1166jwae/JypqVic0v732Zb07+5uBuRtrKYP/7xNOLub95FYsrFic27W3fy8qalVw66tKB9xfxs7x0EUgwzD+MFlsLJ7WfxLbMbTy2+TFm581mdNpoyn3ab26BSyaQNpyGFW4kWWLitCzc/9hJntNISWXnmKBtP5QsIrRDq1+yMH4GK5jD7y4cxUmTx/LP35/FecElLEly8Frpa0zKnERMjfHOfi1l10jvKGzBAia4TmJN4Qe8WvYqMaGNE08rT8M0pxBjVhbp0ThFgSLKUspYVLFocOJJ2EtFxQoAimMxFvo1AUdJN1PlzkUG7mwNcEeGgR1tO0CCrFAW0+WLafW10mZr492SRd3iiaoiGrayq2M7GKDAO4ZIQCE9Np5ri6/lDy1/oIMOntj8BD877We9zPFEPFzz7jU0BBq4aeJNnJanRV+kxw2YJYUStYgXzYVkKj7eKLiCCbGNnBR5lRVGIy/seQFJ0UaPWaEsps88ieETstjyxGRMBe/jxcuWli20RJvBDNmKDTY/h7rq18j+VkIWma0nJTG6MsD8tgBPkEsDMTL9FjTxJBWA8ZPGsHlHAeUp5XxQ8wEPnPYApliYykrNuZSpKERNOWxstWLya+k7BBINdUmcHe8UT6rf58ezfsym5k28XvY6ACe3zCTdP5Hp549kxoUjwN8C5avAkQGjz9MuUDxGRtNWGlKmMjYwjPBEKC8vx2nKxNQyivTM1B7Xs3B8OpZIBsJWg7Ez7cd2eT4BxYhZgCj3My5LZV9zIRmKlvatSwQ6HDXNnRE8UTMhXwxJgozCJEo/2EE+UGsqJMUzBm/qHkbs380Lp17ANc3LOMW7i4tZxe6Wk6nLruPVfa9yy+RbeGnPSwDMDmvOgZ2WMViKpiO1vk2OIlEjC2p8NYMXT/wtULIYfI1wxg/A1NuJM1AWbvonzQbNmXGu2Qn1m6HgyHOO6+jofLF4bvdzPL9HE7Znts7k6hlfpuDNt3C9pU2OyLrr+2TcfvsxmYyTfOGFWMaPp/6uu4mUllJzyy0M+96dfPnLX+att95i+/btxGIxpk+fnqjLkW3NpqigiPkj5ids8ka97O/Y31NUcZcRiAUSywPBYrAwOnU049LHJcSSsWlj+0wJpqqqFpHRWbsjHo+jKAqKoqCqao/XmUom6Wo6E00TUZwKqkNFyVQIxoO0RlppjbTSFmvDFXPhirtoV9rxKl4yY5lkd2STG8jFKDT/SJgwsiyTk5OTiCopLCwkPT29x3sUDcdprfXhbQ3haQvhbQ3hdYXxt4fxtYeJR7Xf2WE1KxhdsRCAfWOvo0GeBJ2pr4wmmaR0K850C850a+dra2JdUqoVIQTulhDu5iDu5gAdzUHcTUHczUGiYQVvWxhvW5i63S04DC6SDc0kG1pIMbeSYXeRYmrFIRoxx3rX8gUQqpVkNY0RahpZShrBpFREUg623EJSikeSPrYYc0Y+2DNhAJmJHCkWTr2smBkXDGff+ia2f1BHR2OAHR/UsXNVHSNPSmfKNAOp7j3E9u0gVr6HWO1+pIgX2aRiMKukmQTpBQLyNR1HMluRbTYkqx3ZZkeyO5BsdmR7ErLDgexIQrInEQgbcDeHcTWHCbijCLWUDPaTbpEx2UwERAa1npF0pI2nI03zJxviYVLfLif1hQcpHJ1M0RXzSJ57JpLJhN1u56qrrmLChAksWrSIzIZMTnOcxoacDaypX8M3l32Tu2bcRY49h2x79mFTxA0Gd9DFvQtv4NNYPcgwKarw1Un3ctmcbxy1YxyMLp4MEHGgvAgYtrqPjyEHoXo8HPwv6nn33UGJJ2UP3tW730DfKZcGghLpua9r9RKc1323z7ZqKIRkNg9qFoGIajl+rdXdES5SuXtQNlZ/51aCqz6meNG7WEaP1myJRqm8/zZyvnEXSRNO7nff8ofu6X3N336bvF8/hNSZY7D91VcS21zPPkvGzTf32VcsFKDp2z/oc9vBCKF9Bgc6cCiZdjLjt23F9fYLvew9GjT85L5+t7me/r9D7itUFWmgae+WrhqMWT2I+7wYnYNLldOxegnp51wGaNfc8+abQz7+oah95IFBtW/IP/OY2KGjo3PsqVKraPG0kJ0ywAhFIaC1RHNi7X0XGrdp6yUZfrAHkvMGb0TIDWXLtT73r4SoD4AVtR+zKFaWaPbP7f/ky2O+fPjfGiGgdR/sW6wJEvWbAHgjeyx0jo0f3/w4ZxScMfA0U6EOKHsf9i3RbIx0Otb3r4DbP2bZ/uU0ehr52vSbBtanENCyVzvnkkXd1xHAns7zpgivl77OwrKFPHnuk5xRcEaP3bsKf/dAVbVz3fuu1m97OXHguwWjqDLHWFqxlL+d/zdm580e2DkfeN4l70LZCogFeT11JKRBZigTe9xOobOQ/ab9tMRaWFy5uEdBxrZQG6vrVnPRyIuwGq2gKlC7QXtv9i0Fl+a4/XtaGotTnRglI78783eUdpSyYOcCFlcsPrx44m2A0vdg31I6KlfTUKh9lg0WP/Z8J5YSCznBHJrtzdy49Ebm5M+hIlIBEhQ3Kuyt0NJWjDo5i9jqOuSYil2WMFV3IJ48Bcm1D4BskQISBCPJnJpUi1yThnPmJGITr+Ir+19lSZKDd8rf5rvTvstu127cMTcWxcII10kUjE4lXH8KuzO30W7V0inlB/I5Y0sdpp8WIkkSmSnJDPOnUZZSxke1H+GL+nCaD1GPwdvQ/fmp+ph92elgszIyGudlZRJqmhnzSelUfaQVw57lbeLc8E3UOerpsHRwStu5XPPj02l+soytbKQ8vB/X7jfJqFgNpe9RE2rFV6QVKh8jpiGAHatqueBsO3O8p7AiYxX/Lf0vXx73Zcand4/tVaHyszU/oyHQAMB/9vyH/+z5DwAj4to4+U1F+zy3GQRtWAiJMfyzw8P7dhvLq7VC3giY3DaTidcX4Ei1UJgxkoJAAVXJVbzw/s9oNGjXcbjXRXj5D7BGFAI2A9umZWLLuIQK5Q2y26L8oKWRn2Zmk+2zAb6EeDJpVjHZ6/KwKBa8US8bX7iEWdVbWFWQCwaYFQ7zfspZyFV+AE4rzmBdhYtgi4QjvQizGqI+2MRu125+ufaX2vl5RzDCNZOzLsxgcso78NyixPcPSPDd9ZA1Ds+775Jd+SEN06bibbVxhVml46pbee9vJVp9meKe/9sWk8LY5GJE+FMwQMQksSesCWQFcZl1r+1n/Jw0SpuKODumCXPvV7/Pd2d8t//vy9Z9ULKI8vq1kArJES2qLy1DYDIbEM1adJbfmIclkonTVwzJFUzraOXesT/i/c3fYpwo54LAaHapdlxhF3cvvonWSCtmxcwVQbf2HkfSyR8zE7bAiFiYGpOZ/a37Obvo7P4/29D9PV66VPuuqN1AYkqtyaYJKINFCGjYwsIdz4ARZkVtjFh5P3ycDPeUgPnoOU90dHQ+3yyuWMyfNv0JgCmuKVw68iJGv/YantVrwGAg98FfkvaVY1uA2jJyJCNe+S9Nv34Yz5tv0vr4E6Ru2cpVt93Km0uXsmfPHvbs2dNrP1mWtSLnnaJK1+tJlknMsM7AnG0mYAzQorbQpDRRF6mjJlRDQ7ABFZVMSyYjHCMYZh1GgbmAPGMeaaQRi8aI+qJE2iJUR6spi5YRiUQSxcy7nmOx2AHWdPkqj0xgyuj8O5jk5OQeQkleXh5Gg5GgN4qnNUTLvhD72yrxtIbwtmmPkC/WxxF6MqL9U4o7hZPA/K9TfNkNTM3oEkgsWB2mAfm+MguTyMy3gS8Kbg90VCPc1SitlSitlUjeWkzhZiQOSqsugANKlMRUCz41CwNx7HIHJjmCWQ5jlhtJpbHnfo2dj7Wd6yQDOLLAmQNJBzycuWBL0yZHhT2JhzHsYVLYw8T8dqKWFuJBL0ZCWJqDsKzHm0Ifb8lBHOS7jXU+vD1XJ3c+hnUt9EU2RC35uKTxVHeMoCE4ilbjaFwZkyiPg/HlIGn/fIb8EXaKL5pJ3umTmThxIsOGDWPRokVQAqfXn86neZ+yy7WLW5ffmujaYXKQZcsix55Dlj2LbHt24tG1PtOWiclw6FR3K3a9wW83/Io2g8AgBBerWXz3qpfITx/C/fEg0MWTAeJvd3E0s8b6Vg3dIXwgxp29RY72f/6LnHvvHXAf8f8u77Wu6uqrGbtxAwbnEAr8HVSkyfP3v0Ef4knc76ds5iyg/+iMLsHgQGpvvY3Uh48saie4SkvDVnHJpYzfuwdJkii771rUJSXUvvPVQ0ZWyFsr+1y/75RTGb9Ny+/d/MCDifXNzz7dSzyJR0KUTZ3e7zEOzhUv4nFKJk9Bykxi3JoNA/oREeEwJf/+FWokdtTFk6bf/g7P228Pef+Kq65iVOdskmNJ2axTE++lf/OnA9qn+Y6fkF6iiSc137+d4Ire+TuPBrH3Dx8pFTdYKBl3Iy3Z/X9WdHR0TnyEJHh1y6vcOe8QNZWUONR8ojmw9i2BjqrubZIMRhvEAlC2nLaJF7NgxwL2tu/FYXLwx7P+2Hdan4Tjd7EWaaLGu7dZUyHs5pFALZg1h2RdUh21wVo+afiE0wv6SM+oxKFmXacTfQm090yr2W5LZZ9dS8NjUA2Uukt5q+ytQ0eyeOo7bXxXizIRB9zYOLIh0Iq/aRd3Pn8zm4WWOrGqpYYHL/xF/9exdr1mX8li6DjwN1vSonc8NcS2v8SrTu1YcRHnhx/+kD+e9UfmFs1FFSoPfPgAb9e8zU3FN/Hj0+7WomD2LtL69Td3dymb+FtyLlVm7SYxJmLcuvxWbEYbZxacye/O/F3fdTXaK7W+9i2F6k96nrclmY/sViDAKPc4CsO50Ab+ZD8tGS28vPdlrh5zdWIscM+Ke9jSsYWPdr3BX+R0pNKlEDhgBp1sYpvNzjMp2mfk+6NuJe39pYwKVEIarGtcR1uojUxbZk8bW/d1i0QNWxKrlzpyQQJn1Mn3gpUMO2sZ32q5jZkNM1mXu4522llRvQIk7XM1JuRg31YtvdGU1EZCm7tTLBUZTbQ3BciwGPFZcskK1RETBlLkVDqA7fv2MTMW45xTphHeUczUcDvbrfD8nucpadNqmgzzD8MeKmS695ekMZFK1zRWF2h1RE6pKsYc24fJpEU1FBYVkRt0kRxNwmv2817Vez2EKECL1Nn7LpQsQtRvxivL2FWVd5IcrLdpttvDmbhxMmtWHldNyOMXW5pQIhJmKcbM2BjOtHwFT7uXc6+eiUkEOHdYCm+5tYL2i5fey9f8Wm2Sv2cUA3GyQllc/KUCtn0Sp64iyJo3G7ikYSd7v1JIXVId9394P69e+SqyJKOqCn9c/VNW169GVmXGecZRklqCkATZkSTudu8nKgwsjJ/Of26Yxl/fXE5u7jZW1M0hLWrnMn+At53aZ6HYV8wk8yySbBHY+S7T7Pv41D2BquQqPlCawKC9z3NjAYxo4/vmqacwY+6/sFrzefn5akZkr+GCliDFAZW6gHbDa0hJhabdpGx7gfR4KvmBfCqTK1nh2YfXasRrgIy4ytxgiG9nTcVQF0ECfnFhEr99w8fHTVHeUc/m1PBbrLHbuG35bfhiPmxxG9NaTyFXkZm44RyQDrjnMDs1UXjbi4hzfonrmQWkuWsYZVzLvOy/IbbCuo0PIokxTJiTp4knwXain65ErvsAY+3bzAulEEOb0FWfZ6XWZQUzTEm3o9QqiL0yJWoRf/EF+FtqCuX+cjY1b2JWrnY/g6pCwxZcu17nzpoP8YsYX/V1sCFTEwzGdGj1brKsWsFdZ7smGhqTCnH464FCLKRx1sdG/vGlXP48/Gv8pOpfXMYqFrvnsDm9grVu7XM/0lfE9LA2Rs0NNjLMkYyKxKhomNV2M2Wt3aJ4D1QV6jZqgmDJol7f46QMA08NbHsZTr8bBjJpS4lB9drE783esI/t+SmAxCVBFUx2iHhhzzsw7frD96ejo3PCoAoVf8xPKBZK1JtQUVGFCoLEayEEAoEqOrd17qvS2a7zdVe7Ol8dD6zVJhOO9oxmfuq5nPTKqwR37kSyWil47M84580bsJ1CCEK+GLIsYbYZuut0DQDZZiP/t7/BfvIU2h9/CLlyObl/XcNdp4wi4GvCL+y4cdKuOHDF7bhJwqMmEwqph6y7cSB5nX+KpKBICma1e2zY0Pl3KMxEScNDNh7SDnwID6l4iWPERRrtIp120mlXM2gnk3Y1gyg2ZNmAwSBjMBoxmgwYTUZMJiMms/YwW02YLUYsNjNmsxGjyUhGeiYptgyUkBFvWwhPXYid29x83NqIty2EEjt0LeEkS4gcRzPpxgZSqMcht2NLtmLNTCZW66Xxow0AZJw7lgkXeiD6V2hQoV4FcfBD9LFO1SYgdVRr0eVqt2AjoTm7ezi8DRZIHYZIGUbUWkBAysEdyaS1xUpTi4NWr5OIasYkwmRKbeRbW8lNcZHsDGGyxDEYIxjkEDIBZMWHFOtACrdDqB1JKOBv0h6DQAIsgOWgj2tMmImqDqI4MNqd2HNyMCRngDVFe5js3ddAVUCoCFUh5Ivga/XjawsS9IaRhIokqUgIjEZwpJog1UDYAh4lhjsaIxiPYxAKxaF6xgarMEcayKOBvM58aSoG3PIIGv3FNMXG0Wwdy/aOAra/2IrpP0vIzRIMP30MX5p7CRMmTGDp0qWcVX8Wu9N3E3FE8Et+wmqYQCxAIBagylt1yGuSbk3vJapk2bPINqfx3uZ/s9i3DdUgURBTuL7oBr72pZ99JmmiBy2eSJJ0FnAvMAPIA64UQiw8YHsO8HvgS0AqsBr4nhCirHP7CKBv7zNcI4R4rbPdMOBpYB7gB54DfiqEiPez7zElFvD3Ek/UeBTZOLhCk13EW3qHhZVfcCGj3ls6pP6OBaWzTgGDgQm7dw1qv9Cbb3FgkLe5USXa3ow5PadHu3333JBw6is+X59CjX/Vh73WRauqaLnxjgHZokajNP3616D0/8UerarCMnIk0W2lh/2HCLbV97tNhMN9rpeavL3WVT3WO9rnQLyLFpFyafcs0H2nn6odo81PuKkKW153nmZpeXWv/RM2/f6/x0Qh7Xj++cM3OgTRvSXs/dOvmPCjX/bbRghB6SmnHtFxAKKuFswZ2VQ+9MMBXwvXqnfwPPlvIntKjvj4g8WXVMTGmf1H9ejo6Hz2SJL0XbSxTy6wHW1cs2EwfayoWcGdHCSeRANahMW+JZogEero3mawQPFcGH8xjLsYNv8bVv0GUbqMu5tXsL11e6Lp09uf5t5ZnZMmEo7fxQfMxu4kawKMv0jrL28qW/8ylRZzGFnInCLOwehbzf6U/Ty+6XFOyTtFK3IZ8UP5Si26pPQ9CLsPsNEMI+dqfY69kNdWPobwLiU1kkp+MJ89aXt4cN2DNAYauWPaHVq0iBDQVppwTtOwtbeN4y6EcRdpKV7+9SW+GZTZIzZ3xqbDGy2vUrxtBNdOuUarzxLxw/73NSGibFnv6zhqnnYdx16gHf/PE1jWsQeXKZOsuEKuYmUnIe784E7OHXYu7d52tro1u14sf5GrP/kbxQf2aUmGMV+CCZew2ZbFvz+6E1CY3jadFmsLdUl1hOIhllcvJ8OWwc9O/Zl23MbtULKYSMkiTC17ek5s6DrviZdRFgvT/uFtSELibPvF+DtkvPEWxooOdqcZKHOXsaRyCRfnn8muLf9mS4cmbHzg3cGrrV6uDbjBkgJjvwTjL8ZTNIv73rkKVQky3JfPBcv/QJ6knc+Lthx2Wi0sq1rGDeOu10SSzs/Pe+F6Hk9LZU4kxI8kGVvBTBh3AYtrPoV4CcmxJE7z7sbkbeWCqRdQ0VbB2Q1n05TZRLWxhmL3SIrc2bhTMlEVwXBLGWzOAazYDSvwx88l1SjjGvEn0q6dTfXiPzN53xOUiiLOGJZPfUMTTcBbL7/Ml7/6Vf5oPYdvuf/F93KzeHb3s9p1EzCqfSIORaVQWkdObj07Wu6hw9qKURjJCM1nw4yrCD2/kZGXZpKT5eHeqmfI8CfzRHoyj216lNNyZ1Poa4G9i1BL3mVRuIF3khw0Gg00Dy8kIssYkRESIFS+2+GmJnw2SpaVW4pKGK1WEMtLY33FBOYY9nD9nGakOaO1/+vNt8PrHzEpLhjuvAh31lZeSs7ihnGX4h11Nks3/AqAqa3TSNvyHCMWltA04S58ySMI+edwydb9/ON0I/t8+7h38Tf4mmrl2aZ1vG/RJhdNc01jtHsihYFCAL4aXc9UKcrb6hzOtm/B4P8Xt52l1X4JCwNv1J/FnR1LWOlwoKp2prSdzLy0NfCH20CNMVaYGed5mE8KzEQN2nTMU9vPZMK4fRjLBBGzTO4ZT2K1aiKAFLmBktw9ZDc3UNTRSMirjbQMqx8gvrsJo6TybbOJ5MAo/pQM7yVnsrMgD3xVXOXzISOzsUEb087O3Elj2fe5fNLprG26hkXuWdxneoU1dhu+mA+TYmJm60zSOyZzhuNJZIMBRnb+b4+/WBMEXrkRtv8Xj2cK0epq0iYIJmQ+ps02tcJ89QE+VL/HnGEZ8O8fEawAX/wazHI6Zuk0kq17MMRrUWTYmzqcKrN2Mz5rRoi4N4mMtghtqSnIipXL/QFeSXbyj63PMGusD/YuIrJvCZ/GvfwiI48Oi3b9fmvVhJNR7blMDs2jCciKrof4deR5tVvi7LzJFO74I7tnfh83eWTJ8JM9Ph6Y8VXmtm9ktncnD3r28AsxE7fZjyIpnBEahkkoVFnyma6WYqhbQ4W1kMK49r9d7Tng/iAehcrV2nfuwQJw1/f4uAu170hLEvxpLLTt074P+ki1tbF0OX5/M9MkSKtaq333ht00Gmw8kpXP5lQJVZKYFDPwpW+vhI3/gFUPw7YXdfHkCDjiscgbt4J9aL4LnQPpPblzKMSFIIJKWKgIBAYkZAEyYEAgCzCgLcuJiZVCG0902dHf665XAkIIvJLAj4ofFZ8k8AkVv6TiQ8UvVHySqq1DwY+KF0Vbj0IQ9Sidcd8U+gs53zuGU157mmhrAIPdSNFXR2Br+Re80rO2q6pK+CMOPKFkPCFn4tkbcuIJOYmr3TPWjYYYFmMUsyGqPRujWIwxzMYIDoMHp9xEktSMXbQiq+2YlA6SVQ+p53WdbQe0NnCoygkRYSYibMSFlYhqIyjs+FUHXuHEoybhlexEJRNRyUBUMhKVDERkI0KSMUkRLLKKxSiwmARWOU4KfhxKEGs8hC0exK76cQgvyZILu+zv24hOn7ERhQKaKJA6nfcHDDJDajLueD7uWB6eeB7ueD4eJR+3kklQ9K4ZJksqZqOfXbE40Nxru4bAJnWQSSXpoopUUYeTZhyGdmwWHxZbGKO5Dx+cF/wlFhrXpIOQSB0dICvzQ/j0w0Nc6YEiaVGTJrv2MB/w2mRHiRuJtIQJV/gJNm2jMmxnvymDqpwCqnMLqB5bQG1OPpaoRJbbTlZHEtkdUbKqomR1uMnucJHV0U6mpwNDYsK4BaRcjDYVczKYnComh8BkVzFYFQxWBdmsEI9CLCKIqzIKEnFkFAnisoxiM0CyCZFsQqSaiCVZ6FBS8URtCFlBMkQxGN1YrHWYTCEEcaSYhF2xYY8lEfXm0tE6irr6KXi9eRwYgSRneAkV+WnKkihNSmG7KYeQ1DuyY0S8AxlBmzAxxV/GdN8epnv3Mt23h5xoO+lqOen2ciahpa8NYaNOHUNbZAwd/jFsWRTh43fqscl+JmWkUG8J42zujsKPS3FChiAWqw+zzY9sDhA1BQkawrSKGM0iRitx4gjaw+20h9spae/HFydJnBkx8/1xX2d8/kRo3gVJuWDPGFDqtKEyFL+qA+3H+l9Aj3w2kvaNvhAtSOhytEChHwLvS5I0UQgRAGrRRJcDuQ1tILC0sx8DsBhoAuZ0tn++s9/eSX8/A9Rgb0W58qkfMuquvw6pv6Zf9nYaR6uqBtWHEh56aq0utl44+dCFxA8q/j4QbPt6iwjlc85OvBY3z0V69qMeToPSWaeQ+eDPyLruph77hdoGXheifeErpF9xbWLZs3olDbcdYpZvJz5PHRZGYmzo/nLfO35Cn9EnZc/+mkMNOTtefpnU667rtb512Utkzf9qYjn27JpebQ6k4d4fk3zJJQkFVXi63+uqeRclbBM9wjU/Z/zjvzSecx5507XZzSIWI1pTg/u113G/9hpqIHBUDlN++lzG79mNcV/H4Rt30vKdz7awc9iSyien/eYzPaaOjs7AkCTpWuDPwO3AeuBuYJkkSeOEEAMuKFUhKli5ZyXnDjtJEyFKFkPFKogf8Jtpz4CxF2pOrFHzeqY3GTsfVv2G9xo/YXvUiVEYmOXNY11KHS/ueYEr2hoZU75GEyYOpPAUzbE44VLIGNVj0/MpI4FqcgJ5pO+ZysSsANVJ1ex17+XJpbfzQ49fqyOgRLp3sqVrtoy7EEadAxZt4kM4HuYN1w4wwQhvAWd7DBRIBlakKvx9x98x+Vv4dljSnHedaaQ6rzAUnQoTLtHsTO+Zo3958iz2mBaBgGuiX2draD1lqSX8cfsfeHzrY9ys5nNnwwakThtjwIakXMqzJzN/yhXkTLxScwYegDLqHP4T2AnAtT4fN3vqeSi1kHdS5UR9EUlIJMWS8Jl9/Dwpl5cNZk3QmXAJjDgLjGZKmku4fclNxGWF7GAOM/Zfjy91L0FrA1brZl7NbeXlkpcZXreN66t30+5v4NGUIpYmS2Tmj+V5Yyb5Ey/THJbp3ZMinn1bi6rJDuZyxXQvgS/PofnZ33NSfDthTzGL0uAXq39KbksbT9iHgxMscQsRY4RHMtPIOuOHnDPzO2A0owqVnyy/g3oliCNm45G2KvKkDirVXCpFPhcFythptfCvjX9h4vKHObmjgRaDgUfTMliSrUWivGpysiFvIr884yGm50yn9NlTQYYi2YIJEKXLuH7abTxhu5qbQ+00tWazXjqZQHQYSZ4JNFrMyMBJtmRUMjDYvfgum0JghY1kVwR7eRINv9tFyK6lxWgTTs6cncm8J7ewYvgw9lRU4Hr8zzSYRpDnT2d0NMp+sxmjamBm20mM8uYxY0wV6nnvYpk4m/PWNxF6K4IkjNiCMnGTzO7yTMwLfk6R8yWQ4GaPmw/tFnYA97w6nycam2g1GPhdRho7nL3zI8Q7Z86eHwjybbeXq5jBmIkerLU/oQ4Yk3U/z5bNZ45hD+q6pzB88pce+xszR3N2YAq71Z3UWwI8XzCNitqtxKU4qZE0rqxpoP6lbZiBKdF1bDWdS1X+uUwMwawGA58W7GK5awvLQbtPFxIzWmcyuf58LJFMTM4Kkg21TDZr//8L1dO4YvZrhMJBTKY0wo1XMUOq4vH45Vxq+IRFtfVsZzJlQTsjxWMEWs2464YhkvI49+oRrKgfRkXKfnIDuXzjrG8R33oFFqAj1UKOrZhofT2bV6wjbetmDPsyKG1TISJjRvs+MxtbMHZGhZilGDeES3g+NowWU4R9viokAVf5/eywjMbnsWA1hrhm0ssApBvWck5BASvrz0AKTOY82z7McTtJ7jMx+ScwPbuR4Zd9B8aeD7bU7os8Zj7YM/CXuWl89lckDw+SO9WDhOCN7PPIiLk5u2MT5zn/iO95K3GrBVNGBjmW7x/4RgNQl2vnEd+9RDAiDBL3mnL49lfTKXqumnEixj5RxE2ecl51Ovmk5VNuql6HKgzsSTcTlzOAKPaYnaSYlRZ7O9a4hZvXF9KQXgBAbnw9HSUrSBMx/AYbY8ZNpzHqJX/XM3jOv4QyZRx17RamrFf4fu4PWR74HiOUFn4SauK9+KWE3YLxqZrPvNw8hhGRBih7jw15lzOicQEAjYE62PWm9ltTtlyL/OjiAAGY0eclvscTjL8Edr0O2/+bEE/iSowXP/od71S+Samx+/5wesTA1wxmWjPH8S9bkEZjDJBJV1SuOelHSPY0mHodrPqNFgHZUQVpI3r9j+kcmqMyFildCpZjPzsXOrPhSBCWZEKSRFCWCEkSIVlb7nodlCSCsoGAZCAgGTGgYhYCi1CwCBUTArMQmITAhMAk0F4LgVHQua7rceCy1s6AQEVCkUA54DneY7n7dVySEstxCWIYiEoyUWSimIhgIiLJRCSIyoKoJIhKEJElIpJ0wGvt/KNd6zqXI3L3OmWQb4UkuoQU7VnqfN0tsHSu69wWlCAkg9qpufR4c+hn3SGPLyEhgUB7RnuWRPfrxPPBbTrt7zrlzjVkhLI4q2UUpy97D7wxTI44eWe1E3KrNLXl4la0h0fJwxvPxa9kI/pwYRoAswwOg0AVEnEBcVXGEPeRLOpJoQ6HVEeqVE8m9SSrvSe3duETNspFHuUin3I1n0aRQabkoUBq63y4KJBaSZGCWKQoFikKeKCPLPQxxUAobCIeMIAP4gGZWNCAUCSMSQIp1YzRCRZ7BLvFhywdJDYc5Af2qw46RDIdJOHCQbNIpU5kUiNysEthimmkSG4lT3KRJblJw49dimKTvdjMXvLo7YwOKUn44lm4Y/m0K0W0qyNwx/PxxbJJkl2kUEe6WkkatSTLzTiM7djNXizWEAbj4T84QcVMu5JMq5qCSzgxtUTJWu9GEhDOM7F/XC4VwRwMkopsUDAY4xhNCgZzHINJwWiOI5sUZKOCagBFlrSISO1jhmKQCFkNhCwSqixhUgSmWAxCXqLeCMGOKDVRJ1VKDnXGfBptObSMyaTt5DTiGEERoAokRYWwgMooYVnCY8ymLDUHMmWEUQJj97NkEKTGvGRG2smKukiPuchQXWTQRprBRbq5jRRrBzhkMB86BVU3CjFVIhQzEoxLhOJRQpJMMGYnFEkmGLARclkJxm2E4jYU1YDNGMZmDGE3hbClNmHKrMVNFm1SAa2GHOps+bTZhoFB6hFF6oz7E8LIdO8eTvbtJTOmpUoOyWbKbcPY5xjB1uQJ/DfnAjpMyWRH25nuK+Fk3x6m+kqxqyHGyDsYY9tB18z5FkM21YylOTYGZ8doYtEMMLdhdDSAxYfJHMJBCGc4QHLQT5rqITPeQWbcjUkoCKBDlmk1Gmg2GGg1GGgxGmgxGGgxGmk1GIhJMmfF0vleyx6MDQdlIZCNWtYCZ44mpvT3nJQNh0kN1hdSX2mRBryzJAkOiDyRJGkssA+YLITY3blORhNBfiaE+Ec//WwFtgghvtm5fCGwCMgXQjR3rrsdLaIlSwgR7aufg/pMBjwej4fk5MHVPOiL9d8+m+SPequufTnYlVgMEQ5Qe+9dFPzs15iHDevaALEQIhaiZNbZAz62MS+H0Ss/6K4RIQTEI4Tq91J1wVf73S+aYUAdmYl5ezNyDFSHROrjv6PgjMs1cxSF0kmTD3v8nMcfIX3+5YnlXadPwuDSvtitP7qMEd98RPshVKJsuf86bAuHPlvfNHMyo59/RXMmxcPsnd5H2pBDMHbbVgxWK+HSUiovu/zwOxyCcdu3oQYDuJa9Rva1tyGpcfZOOmnI/RW+8izxPRU0/eqhAe9jnjyWzO9/v08RKOnai/G/sriPvT5fRG+5CvO/3jjeZhxXKkZcTNWIi463GTonMIboVm7/1z1HpS+v10tKSgpAihCi/7sHHQAkSVoPbBRC3Nm5LKNNBHlSCPHIYfZNBjzn/f5KGnNrSI0msbhhXyL9DQCpwxIzftszRuGPBilKLeodfiwEnr/O4JpkE24jfNvt5ha3j59kZfChw05mDK72eymIgylzPElFs7CNOB1bciHDkof1yh+rqirzXjibsCHCmVXzmR32UmzaSZWzld9na6PgC70RZkb97LcV4nYUoFozGVc4kzmjzmBkZrezf2PJFh5Y9wvazW1IAv5e52Oq4gbgdaeDP2akIwl4rLmF08IRbabziDOIj/kSq3CwomY9NpONuaPmcsaYMzB3RvUKIbjs35fRYmmh2DOMl7/yW7a9v4pH2z+mJqmasFFz1I7wp5Op2Gm0RGk0t6HK2vWVBEwwTea7c+5gZlGnA1CN89N3bmF1YB9mVWVBbYh0VSVbcrPe7OAF6wS8spMCTzGZcRuvFr+NkODC3Av56dyfYjFaEEKwYP0Cnit7jrgcJzmSwiV7votJBEiz7GWe7S1y5XaeSk3m+VRtzqIzDj4DPdJR21U7N467kenDplPgzCfDlsmHpR9y/6afo0qCM5smc5naxrTIbpIlbRKFCnw3q5Atjp6fjwvLL2Zr7iaaHM1IAuYXXMDIjJFsbNzIprZNyCo81djB9JifJpHGb03nUeCdyLWOP3NXfhJNJs0ZkRaX8BkgLgkQMMmbTaWjnaBR8ypbJSthEUZWZe7uuJasWj9xyUKaZTszLavQbg00OmIZuPzDqJKuosBaRJqk4pfb+b+8f5Ic85EfHsnZ7qswS9l45BKGmf5EihRgTfR2CtPDrJ18Cs+2W2hIyyLH206mq53k+kZ+bv8L7yTZudQXZlS8W9hThUwbBXiSRuILO4g2dZDkbsBaaCbd3EG6QUsd9kL8PJaop/Ad6394qEDBazBgFIJ45/+cWYWL3Abyw3ZS4zJjlA6cxhZaTDJTwxEejV3LggnXcX/ubxhJNU6RxjJpPM9vvZqV/h+QL7mICQNkj6c8nocx2oHJloLqHMYTLbV8klWKJKDT38T5TWfyzcXLMVsUkk4ZS8rEZFrK22gJ5OKKF2Dw1bM2T2FZURUhQ5jcUBYnd+Qz1ZvCWMsOcuVaDMRJlrQ6RmVqAe+OHcv0nO1kRUYhRv2UYNUOPt2YxEZnHcmtKk+ZnwAgLNkJNzmJtKcSy05DtrqxGlqptObxhtPCSZEZXDWhDdP2N4l6jdTuSyHqSkP2957gIgyClPwQqaODGNMFC5U5vMKljDa183P1MULGGE8m57M2CeYHfPyk3c0T8Sv4P+VyvjpmBXOtISp2nUbu9BdQHO088MlPGavU86L5d0gIFGEgTAZxOZ2IMgpjylScF87HNGKYdhMsSfh+cx3Brdsx5Sqk5QeRELyQewm/zvomCMGDjQu43tUzyj8qTGxUx9JKKtPlMuzGIHcX3MWmhnHIAYVkZ5jWUzVR9+ZoM/6VgpOsz3ODcSV/Ss/gtWR7j/4scQuF3nQu/zSLlKCVTyZ6GNVoQcq6iXBIMDZzL3MMv6UpfTzD2nexJ2k0lZExPNk4lxpnzyj9Lk6XdvKM+TEkBPXqFJqMyUxgE3Y1wrqTfsppO34HkoXar7xF+O2vclNuEkKS+IHLx3U+t9ZJUrYmMI27AIafAcb+HQetu97ipY9/j99oZnLuDHb4qlkXq8fV6Rw0CEGyKujoIy1OTlzly8Ov5cpTbyfFdoBw/dK1ULkGhs+BKVfjLV1L/vVPgz4WGRBHYyxy89+/gsVmIuHJpsufpnm1JbTvpc6pewd0IDrXHOD9RhAVCiERI6RqzxE1TkTEiBAnpknOOicIkgCTakw8zKoRk2LEpBowqwYsovu1Welcp8pYVBmrasCqGDAKCQMKMioGSXuWUZBRMEraayMKBqFiQMEgqRjQXhtRMKB2PiuJdQByHAQGFMmIIhlBGOmMvQFkJKSuuBykzrgczXcuI2PAiBEZQ6dIIyFLrVilBtKkJoxS/xNNG0RG50SSPCpEHm0iD5+Sj1DSSFVlklWJFEXCokoEEHhl7eGTBT4ZFClAkqGNFIOLHMlFgeQiX2olX3KRJ7WThafHmGggRIWRepFJnciiTmRR2/VMFvUiEz/2w3dyEA5CDJNaGE4zw6UmRsjNDJeaGSE1kSod+WTVFpFCo8igQWTQILKo73zdiPYcOCAnTbG7nl+v+wf2eIRN2eN4ZNaNKPLAax+bpQhWYwSTIYbVEMVqiIIkiCgmIoqFsGIholiIqUaEOHYRCF0I0IQJo6x9bA8QWDCAxRDDbgpiNwQxxFWIgVAkhCKjxLVHPGYgFjcQiRtRjpnNAqNBxWaMkWyMkGZQSJENJEtmnJKJJEnCgSY+2gwCm0nFblJxmFTsJoHdrBWqb7GYqDGaqcRIMNhGkreKIm8503wljAnWIB1BjJpAotWUSqspjQ5jKj45hYg5GZPdSZIjmQynkzSrgyyDhDncCr4WCDR3PwdcDDwqUAJ7OiTl4DWkkX/bWzCAscjRFk+mADuA0UKI8gPa1QIrhRA399HHDGATcLoQ4pPOdQ8Blwkhph3QbiRQAUwXQmw9uJ8++j2q4snfvnklTncz5rCPjrzu2TmqJIA4JiGj9CU36+jo6AyAz2YemM7njeLyEPuHO2nMmsJDf3zqqPSpiycDR5IkM1oVvqsPSlH6HJAqhDikSt81Fhn++jvIdr1Iro6Ojo6ODoAaDFB99WWgj0UOiz4W0dHR0dHROfoMZixytMshlAA1wO8kSfo2EAB+ABTSO1VXF98E9nYJJ53k0ju5XvMB23ohSZIFepQlGUKl8/4JpJqZt7Yz7U/5wNP/6Ojo6OjoHAmFjWEWXlx7vM34XyUTLRC/rzHJ+IMb9zcWsbf+BINNn2Cho6Ojo6MDoIQGnxr6fxh9LKKjo6Ojo3OUGcxY5KiKJ0KImCRJXwb+CbSjpZB8H62WSa+J1ZIk2YCvAr8+Cof/KdB/9ekjxG7sjl7ZPdaYOBkZlThafkyz0OeOn2gcy+JmOjo6Oscam4jQ6rQgUi2Hb6xzInBMxyI6Ojo6Ojo6OodBH4vo6Ojo6OgcRY525AlCiM3ANEmSUgCzEKK1M0fnpj6aXw3Y0YrBH0gTcMpB63IO2NYXv0MrotaFExh4tfHD8N3fL9AqrgATjlanOjo6Ojo6OicybWgTQQ5ORJ9D3+ORPsciv828B4d98HmKdXR0dHR0vogEgkGu5FvH24zPC/pYREdHR0dH5ygzmLHIURdPuhBCeAAkSRoDzAR+0UezbwLvCCFaD1q/Dvi5JEnZQoiWznXnA15gTz/HiwCJqpG9Cq3q6Ojo6Ojo6AwCIURUkqTNwLnAQkgUaT0X+Gsf7fsci5zzpa8clfprOjo6Ojo6XwS8Xi/o4smA0MciOjo6Ojo6R5/BjEUGLZ5IkpQEjD5g1UhJkqYB7UKIGkmSvgK0otU+mQI8DiwUQiw/qJ/RwFnARX0cZjmaSPIfSZJ+jFbn5GHgqc7BgI6Ojo6Ojo7OZ8GfgeckSdoEbADuBhzAv4+nUTo6Ojo6Ojr/M+hjER0dHR0dnePEUCJPZgKrDljuCgl9DrgZrTD8n9HCSBvRUnL1VdPkFrS0WssP3iCEUCRJugR4Gi0KJdDZ/wNDsFdHR0dHR0dHZ0gIIV6RJCkLeAhtMsc24AIhxMGFW3V0dHR0dHR0jjr6WERHR0dHR+f4IQnxxSypLUlSMuDxeDx6eKqOjo6Ojk4nXq+XlJQUgBQhhPd42/NFRh+L6Ojo6Ojo9EYfi3x26GMRHR0dHR2d3gxmLCJ/Nibp6Ojo6Ojo6Ojo6Ojo6Ojo6Ojo6Ojo6Oh8PtDFEx0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dnQPQxRMdHR0dHR0dHR0dHR0dHR0dHR0dHR0dHZ0D0MUTHR0dHR0dHR0dHR0dHR0dHR0dHR0dHR2dA9DFEx0dHR0dHR0dHR0dHR0dHR0dHR0dHR0dnQMwHm8DjjVer/d4m6Cjo6Ojo3PC8P/t3XvUJFV5qPHnZYabF1AMMojKIBCIII5iEBAMggQ9ChgxJnoI92DAnIMhokdjADFqRI3CkQiSuAgiAiqQGBVQxAsR8BaWgjBZeECRcBG5j8MMw7znj71biub7Zmpm+t7Pb629vq+rqnfv/e6uS9eu2uV+cfCMuSRJj3G/OHjGXJKkx6zKfjEys49FGZ6I2Az45bDLIUnSiHp2Zt427EJMMo9FJElaIY9F+iwi5gM3D7sckiSNqJUei0xy50kAzwIe7FGWT6WcAHl2D/OcVMaqPWPVjnFqz1i1N82xeirw3zmpBwEjoh6LLARe0uOsvwfsNML59TrPfq2ro17vfuTX6zzHpW1GPY79yNO2Gd38+tE24xDH7jw9FhmAiNgAuJ/R3xb0I89xKKPb6tHNc1zaZlzydN2ZrjzH5VjnB8A2KzsWmdhhu2rFe3YVSzn/AcCDmek9rytgrNozVu0Yp/aMVXtTHqtpq+9QZGZGxLJef78iYnkv8+x1fr3Os1/r6qjXux/59TrPcWmbUY9jP/K0bUa3jP1om3GI4wx5eiwyWCO9LehHnmNSxs6/I90+4xDLXuc5Lm0zLnm67vTOOOQ5Rsc6y9pcxOED4yVJkvrntDHIcxzK2A/jUO9xKGM/TGscbZvRzHMa22Wc8tRwjMP3YxzK2C/TGstxaJ9xqfc4fIf6YRzqPS559trQ6j2xw3b1WuN21w2n8ArlVWKs2jNW7Rin9oxVe8ZKGg+uq6PLthldts3osm00SH7fRpvtM7psm9Fm+4y2SWsf7zxpbwnw3vpXK2as2jNW7Rin9oxVe8ZKGg+uq6PLthldts3osm00SH7fRpvtM7psm9Fm+4y2iWof7zyRJEmSJEmSJElq8M4TSZIkSZIkSZKkBjtPJEmSJEmSJEmSGuw8kSRJkiRJkiRJarDzRJIkSZIkSZIkqcHOE0mSJPVVRLwrIr4fEQ9GxF0RcXFEbNO1zHoRcVpE/DoiHoqIL0bEJl3LPDcivhwRv6n5fDgi5s7ymS+LiGURcW0fqzb2Btk2EfHWiLghIhZHxMKIOGgQdRxXPWybUyPihxGxZGXrQ0RsVT/vvt7XaDIMsl0i4o0RcW1dr34eEcf1sWoaUQPeTu8RET+q38ubIuKQAVRxbA2qbWq75Axp3qDqOo4GvL3eISK+ExEPR8StEfGOPlZt7A2qbSJi/izrzs59ruJY60X7RMQLI+JzdX1YHOU3wDEzfNbI73fsPKkiYv1hl2EcRMTmEfHs+v+cYZdnlEXExhHxtIhYq752fZtBRKw37DKMi4jYOiLe3r3T0hO5TZdGzh8ApwE7A3sDawOXRcSTG8t8DNgX+OO6/LOACzsz63HHl4F1gF2Bg4FDgJO6PywingacDVze85pMnoG0TUQcBXwQOBHYDjgBOC0i9u1PtSbCGrdNw6eB81f0YRGxNvA54DtrXPLJNpB2iYhXA58FTge2B44G/ioi/rI31dAYGdR2eou6zBXAAuDjwD9FxD59qdVkGOjxDbANsGkj3dXT2kyeQW2vNwAuA34O7AgcB5wYEUf2phoTaaDHOMArefy688M1KfwU6EX77EjZRh1IOfZ/P/DB5nHM2Ox3MnOqE+UL8Engq5Qf2TsDMexyjWIC9geWAxcPuyyjnOp36nTgBuC7LVJCsgAAFdpJREFUwFnAnGGXa9QS5eDwY8AX67q3+7DLNKoJmEPZcT0M/DOw27DLNKrJbbrJNB4J2BhI4OX19YbAUuANjWW2rcvsXF+/GngU2KSxzF8A9wPrdOV/HvA+yon6a4dd33FK/Wqbekz04a7P+ihw5bDrPC5pddqm6/0rXB+ADwGfoZy0u2/Y9R2X1K92Ac4FPt817X8Bt3psM92pj9vpDwHXdX3WecAlw67zuKQ+ts0e9T1PG3Ydxzn1cXt9FHAPjeNR4O+BG4dd53FJfWyb+fU9C4Zdx3FOa9o+jWVOA77ReD0W+52pvhK+3uJ4DbAD8KX693RKL7F3CjzRTpR4PSciDgDvPukWEVsB36dcEXI08BVgF+p3SkVEvA64idKz/M3694Od75We4FjghcAfZObhmXklQETEcIs1WtymS2Nlw/r3nvp3R0rn59c7C2TmjcAvKPtR6t+fZOadjXwuBTagXM0EQEQcCjwPeG9fSj75+tU261IuAmhaDOxU73jQyq1O27QSEXtSrhx865oXc+r0q11mW2eeDWy+WiXVpOjXdnqXZh6NZVZpezLl+nZ8U10bEbdHxNci4mW9LvwU6Nf2ehfg25m5tDHtUmCbiHj66hd3qvTtGKf6tzr81JURsd8alXQ69ap9NmzkAWOy35n2E0kvo1z9/sbM/EfKbUYXAe+NiO0yc7knJx93wnFDSsfAfwLHRMTamfmoMXqcVwMPAftm5hXAyZRbN+8faqlGSERsSblt79OZ+YrM/L/AXpRe662HWrgRE8WTgT8CzsrMayJil4g4MiJ2A568kiymjdt0aQzU44qPA/+RmdfVyfOApZl5X9fid9Z5nWXunGF+Zx4RsTXlSr8DM3NZb0s++frZNpQfQkdExI51//YS4AjKD6/f6VklJtQatE2bvJ9BuVP6kMx8YI0LO0X62S6Udeb1EbFXRKwVEb8L/HWdt+nql1rjrM/b6dmW2cAhcVeuz21zO+VulANquhX4ZkS8uFfln3R93l63aUPNos9t8xBl3/nHwGuAK4GL7UBpr1ftExG7An8CfKoxeSz2OzM+YHPSRcRambmcctvR0zPzNoDMvD8izgB2A86gDI2TQyzqSGiccNwKOJ4St5MptyaeSvnRu3T2HCZf4zv1O8C8zHyoztoEeDqwKCK2rT2xUykioq5P6wA/pgwLQUTMycxfRcSjwJbDLOOoycyMiGdRrqC+JCI+CrwJuJmyPv44Ig6Y9hMdbtOlsXMaZfz+3XqZab0b9lzghMz8r17mPUX60jbV+yg/kK4GgvLD6F+Ad1CGhdWK9bNtzgTOzcxv9yHvSdfvdtkS+HfK760HgFMoQ5O4zkyvfn7ntGb61jaZuRBY2Jj03XpR4l8Bf9brz5tQrjujq5/rzt3APzQmfb+eYzkO+Ldef96EWuP2iYjtgX8F3puZl/WqYIMyNXee1Cu13xwRW9WTbFDGlbwjInbvLJeZd1CuWPz9iNi7vndqrlRuxqkxbU494fgo5fbxqylXcx8eEecAx0bEusMp8fA0YrV14zt1LbB+RFxSY/MzYAnwNuAbEXFYfe80fad2qv+uBZCZN2TmSZl5c339aESsAzwJuGpIxRwJnVh1DS/1S+DXwN9RhmjYC9iv/t0ReM80fZ86IuINEfHKiNjUbbo0PiLiE8BrgVdk5i8bs+4A1onyoPemTeq8zjKbzDC/M++pwEuAT0TEsohYRrno44X19Z69q8nk6XPbkJmLM/Mwyv5+PvBc4BbgQeBXPanEhFrDtmljT+DtjfXmn4EN6+vD1qDoE63f7ZLFO4GnUI4B5wHfq7P/3+qWW+Or39vpFSzzQGYuXoOiT7wBtM1Mvke5oE4rMYD96Oq24dQbQNvM5Bpcd1rpRftExPOBy4FPZebfdS0/Fvudie88iYh9IuIuyl0SHwC+EhHH1tlXA+sDu9aTtx3XAZdQe/Cn4UrlWeL0Nvjtye2NgBcD12Tmryk/fH8XeD3wtcxcMpySD94Msfpy4zv1r8C+wGcpz4h5U2buRvlR+gng5IiYOyXfqddFxG2U79L8+j2a05jfPIG9DuWugesHXc5RMEOsljditR6lU+n1lCt1FwL31tsljwOOrMtMhYj4s4i4k1L3c4HPR8Tr6+wfUGIx9dt0adSUUZriE5RhCPfsdKA3/BB4hNIx3HnPNpQT7J2O9auAF0TEMxvv25tyNfZP698XUJ6j1UmnU7abCyg/lNRlQG3zW5n5SGb+MjMfBf4U+PdGJ7gaetQ2bezC49eb4ymdWgsoF0ypYYDtApTfYpl5Wx1L/03AVZlph+MUGeB2+qpmHo1lpvoCtxUZ9D60ywLKcF6axQC311cBL4/HP8Ntb2BhZt67WoWfcIPel3ZZgOvOCvWqfSJiO+AK4F8y829m+Kjx2O/kCDy1vp8J+DxwRv1/a8pYd8spz6QA+EdKj/0eXe/7AuUZA0Ovw5Dj9BpgDvBM4ALKj9wfU64Q/BJwA/D79X1zhl2PIcfqtcBadfr/pnQ0AUT9uztlvMVdh12HAcTof9b16nPAd4DTV7L8PsB/U4Zc6kzbZNj1GJVYUX4o3w1cXF/PqX9fCtwFvHjY9RhAnOYCx1B+QBxO6XDblTLky1eA9etyZ1BOkO7R9f6p2qabTKOW6vHWfZRnEc1rpPUby3yS8pywV1DurPsu8N3G/DnATyjPAXhh3XfcBXxgBZ97InDtsOs/ymlQbUO56ObAeuy0E3Ae5c7K+cOOwaimXrRNXWYrntiZuABYZ5bPPQS4b9j1H9U0qHahDAf8F8C2dfoplAfG7zTsGJjG7zvXcju9BbCIMkT3tsDRwDJgn2HHYFTTANvmbcD+dbuxPeX5A48Cew07BqOcBri93pByBf3ZwHaU5zosAo4cdgxGNQ2wbQ6mnE/ZtqZ313Xn0GHHYJRTj7Zt29dt2We68ti4scxY7HeGXoA+NXLnZPUWwL3dQafcFfBflAPSZwI/olzBvFljmS8D/zDsuoxAnG4AngVsRukgWEq5g+JpwPOBrwLfGXZdRiRWPwW2rK/fQelc2qCxzLuAbwFPGnZ9+hin5kn9D1J6nY8DbqSezGaGTra6ozu3/v8iSs/0hdTOqElMLWPV2eE/GfhYXQdf2cjjr4HLJjlOjbpuSBm67J3N+tbXVwIb1tfzpnWbbjKNcgJylnRIY5n1KGPq3lMPoi+kPEesmc/mlA7T31Au5PgIMHcFn3sidp6MRNsAvwf8Z51/P3AxsM2w6z/KqYdt881Z8pk/y+cegp0nQ28Xym/VqygXXy0Cvg68dNj1N431d26l+1Bgj7qtXkIZgvqQftdvnNMA96HvAG6idKD+mvJ7+RXDrv+op0HuR4EdKBdDPkwZevudw67/KKcB7ksPppyrW0Q5/rwGeMOw6z/qqRftQ/kdNlMet3R91sjvdzonhCdCRGwN3JS1UhGxHqUX7D2ZeWZErJOZSyNiQ8pV7u/LzL+PiDcCf0k5eXkqpZdyH+CAzLxyGHXpp1WM0+3ASTVObwJ+lpnfa+T1FsoY4x+FyRsOZzW+U+/NzJMj4iDKd+o+ypXw/4MynNffZuYZw6hLP3XHqU6bm5nL6m16H6Ac/L2mzotGTNeibGSvpBw0Hg2cAxyRmY8MuCp9txqxmpNlyLMtKDufAyhXJS2hbKfelZmfasZ0Usyw/i0AflLjsVaW4c3eTOl0emmW4SyIiDdQ7v6aim26JEmSJEmSem8innkSEW+MiJspV/pfHY892HAOZZz7AxonudfOzPsptz0fBZCZF1Bu47qUMrTSM4CXT9pJttWM08d5LE6f63ScNJ5X8U+Z+ZGsBlqhPlqD79RbATLz7Pp6XcottvOA3Set42QFcYJyKySZeT3l6tL5EXFo562N5TajPAD9ZMpzdbbPzIMnreNkTWOVmTdn5sGUu01+RrmiZdfM/FSdP8nr3+EAmXlts+OkLv4aylXlSzvPOcnMLzAF23RJkiRJkiT1z9h3nkTE3sCHgA9TxsO/EjgjIv48MxcB36AMzXVIfUvnBOOFwPoR8RKALA/hewvlAd+vycyFA6xG3/UgTjs28+ucqM3ysM+J0oNY7QSQmZ+lPPjoDVP0nTo9Iv48ItbPzIyIuXXxyyjDDhwVEU+pdwx0Hui9AeV5On+YmS/LzBsGXJW+W8NYLWs+eC4zz8jMd2TmYZP2nYJZY/XJGqv16mJZH2C2HmUczcsBOnee1P8nepsuSZIkSZKk/pq78kVGU2OIml0oYz6eWa9Uv7SeUDsqIn5OOaG9N3BwRFyWmbfULJ4HPFLf+1uZ+fCg6jAIPYzTPYMv/WD1MFa/6uSZmcuAOwdYjb5rEacjKQ83v6jWn8y8LSIuojwA7+0RcSHwgYg4qt5t8adDqUyf9TBW74+IozPz1uHUpP9WMVadYbw2onS+XVNfbw0clZnHdvKdtG26JEmSJEmSBmNs7zxpDFHzfMpzOB5pXJ39HsrDag6kDIdzGuVBy+dFxK4R8VzKMyh+CNwx2JIPlnFqz1i10yJODwP7R8Q8KM/sqPOuAL4HHE+J01zgroEVfAh6GKu1MVaPi1X1SuBW4PaIOIXyILjNI2LtxtCCkiRJkiRJ0iobm86TiNg7Ik6NiLd1hkWqLgdeXR+q/Eh9/sS9wNmUK5hflJlXAUdQTtZ+mnJScgfguMxcPOCq9JVxas9YtbMGcdoGytBuEfFkyp0DbwG+Bbw4M1+VmUsGXJ2+MlbtrUGstq3vD+C1lGG7bqEMkbdLZh6QmY9M0jNgJEmSJEmSNHgj33kSEZtGxJeAc4CNgMOAyxon274FPACc0HkLQGaeCTwF6Dx/YiGwB/AqYP/MfPEkjYFvnNozVu2sYZw2AF7UyG5zytBch2bmKzLzJwOowsAYq/Z6EKsFdfr6NS0C3pqZ22fmDwZSCUmSJEmSJE28ke48iYgnAR+knBzbOTMPzMwdgIXAUXWx24FPUp4N8JzMXNoYrmUhZQiYjkWZeUtmXjOgKgyEcWrPWLXTozht18kvM3+amTtn5mcGV4vBMFbt9TJWmfkb4MTMfE5mnj/QikiSJEmSJGnijXTnST05tgQ4KzNvjojOA+6/AvxefcDwg8C5wI+ACyJi88zM+gyKZwIXN/KbyGFcjFN7xqqdXsdpkhmr9vqw/v1wsDWQJEmSJEnStIhRP/dbx7t/pP6/VmYuj4jPUq74P7Kx3GbANynPoPgBsCtwI/DmzLxz8CUfLOPUnrFqxzi1Z6zaM1aSJEmSJEkaByN95wlA5yRb/X95/Xdz4D+gnHyrJ+BuA14N/B/gVuDdmbnXtJxkM07tGat2jFN7xqo9YyVJaiMizoqInCFdUuff0pi2uL6+ICL2nCW/9SPinoi4OyLWrdMOmeUzmml+RJw4y7wbBxkTSZI0OB6LSIJyRe9YiYjnAVsB10E5+RYR6wBLM/Mm4CZg6se/N07tGat2jFN7xqo9YyVJWoFLgEO7pi1p/H88cCawDjAfOBD4ekT8bWa+v+t9BwDXAwG8jrJvOb9+RseFlP3R8Y1pv6p/rwde2ZXnsvZVkSRJY8hjEWnKjU3nSR0LP4HdgIc6Y91HxAnAvIg4ITPvGmohR4Bxas9YtWOc2jNW7RkrSVILSzLzjhXMf7Ax/xfAtyPiduCkiPhCZi5sLHs4cA7lhMXhwPmZuRhY3FkgIpYCv+n+zIgAWLaSskiSpMnjsYg05UZ+2K6OfOzhLDsBX4yIvSPiZuBo4CJPshXGqT1j1Y5xas9YtWesJEl9cgrlpMT+nQkRsSWwC3BBTbtHxObDKZ4kSZpwHotIE2RsOk8AImI9YB/gOOBLwOmZuUlmXjbcko0W49SesWrHOLVnrNozVpKklXhtRDzUld69ojdk5j3AXZShMzoOA76amffW+ZfyxCE4VuYFM5Tl9FXMQ5IkjRePRaQpNzbDdgFk5sMRcQvwNeDYzHx4yEUaScapPWPVjnFqz1i1Z6wkSStxBXBU17R7WrwvgASIiDnAwcAxjfnnAB+JiJMyc3nLsiwE9uua9kDL90qSpPHksYg05caq86R6VWY+OuxCjAHj1J6xasc4tWes2jNWkqTZLMrMm1blDRHxDGBj4OY6aR9gM+D8Ol54xxxgL0oHfhtLV7UskiRp7HksIk25sRq2C8CTbO0Yp/aMVTvGqT1j1Z6xkiT12DHAcuDi+vpw4DxgQVc6r86TJEnqJY9FpAkyjneeSJIkSZp860bEvK5pyzLz7vr/U+v8tYEtgAOBI4B3ZeZNEbExsC+wX2Ze18wkIs4GLoqIjerY4yszd4ayZGbeuaqVkiRJY8NjEWnK2XkiSZIkaRS9Cri9a9pCYNv6/0k1LQXuAK4G9srMK+r8g4BFwOUz5H05sJhykuPUFmXZboayLAHWa/FeSZI0njwWkaZcZOawyyBJkiRJkiRJkjQyxu6ZJ5IkSZIkSZIkSf1k54kkSZIkSZIkSVKDnSeSJEmSJEmSJEkNdp5IkiRJkiRJkiQ12Hki6Qki4qyIyBnSJXX+LY1pi+vrCyJiz1nyWz8i7omIuyNi3TrtkFk+o5nmR8SJs8y7cZAxkSRJkiRJkjQ97DyRNJtLgE270psa84+v07YBDgLuA74eEX8zQ14HANcDNwKvq9PO78r7KuDMrmm31mWvn6Esu61xDSVJkiRJkiRpBnOHXQBJI2tJZt6xgvkPNub/Avh2RNwOnBQRX8jMhY1lDwfOAaL+f35mLgYWdxaIiKXAb7o/MyIAlq2kLJIkSZIkSZLUM955IqmXTqF0kOzfmRARWwK7ABfUtHtEbD6c4kmSJEmSJEnSytl5Imk2r42Ih7rSu1f0hsy8B7gLmN+YfBjw1cy8t86/FDh0FcvyghnKcvoq5iFJkiRJkiRJrThsl6TZXAEc1TXtnhbvCyABImIOcDBwTGP+OcBHIuKkzFzesiwLgf26pj3Q8r2SJEmSJEmStErsPJE0m0WZedOqvCEingFsDNxcJ+0DbAacX59d0jEH2Av4Wsusl65qWSRJkiRJkiRpdTlsl6ReOgZYDlxcXx8OnAcs6Ern1XmSJEmSJEmSNHK880TSbNaNiHld05Zl5t31/6fW+WsDWwAHAkcA78rMmyJiY2BfYL/MvK6ZSUScDVwUERvV56CszNwZypKZeeeqVkqSJEmSJEmSVsbOE0mzeRVwe9e0hcC29f+TaloK3AFcDeyVmVfU+QcBi4DLZ8j7cmAxpcPl1BZl2W6GsiwB1mvxXkmSJEmSJElaJZGZwy6DJEmSJEmSJEnSyPCZJ5IkSZIkSZIkSQ12nkiSJEmSJEmSJDXYeSJJkiRJkiRJktRg54kkSZIkSZIkSVKDnSeSJEmSJEmSJEkNdp5IkiRJkiRJkiQ12HkiSZIkSZIkSZLUYOeJJEmSJEmSJElSg50nkiRJkiRJkiRJDXaeSJIkSZIkSZIkNdh5IkmSJEmSJEmS1GDniSRJkiRJkiRJUsP/B+87pUzMXF29AAAAAElFTkSuQmCC\n",
      "text/plain": [
       "<Figure size 2000x400 with 3 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "cat_data=one_hot_encoded_data\n",
    "df_inf=cat_data.resample('1m').mean()\n",
    "df2_inf=cat_data.resample('1y').mean()\n",
    "#check for seasonality, trend, \n",
    "fig, axes = plt.subplots(1,3, figsize=(20,4), dpi=100)\n",
    "cat_data.plot(title='All influenza', legend=False, ax=axes[0])\n",
    "df_inf.plot(title='Influenza seasonality', legend=False, ax=axes[1])\n",
    "df2_inf.plot(title='Influenza trend', legend=False, ax=axes[2])\n",
    "#data['AH5'].pl"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "a3e23a55",
   "metadata": {
    "_cell_guid": "19e19b56-d76b-42af-9716-bb1f519f496e",
    "_uuid": "19e2048a-b1c4-4604-9b80-d860bf3a3bcd",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:24.606920Z",
     "iopub.status.busy": "2022-05-01T20:48:24.606617Z",
     "iopub.status.idle": "2022-05-01T20:48:24.628084Z",
     "shell.execute_reply": "2022-05-01T20:48:24.627131Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.048199,
     "end_time": "2022-05-01T20:48:24.629997",
     "exception": false,
     "start_time": "2022-05-01T20:48:24.581798",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Year</th>\n",
       "      <th>Week</th>\n",
       "      <th>SDATE</th>\n",
       "      <th>AH1</th>\n",
       "      <th>AH1N12009</th>\n",
       "      <th>AH3</th>\n",
       "      <th>AH5</th>\n",
       "      <th>ANOTSUBTYPED</th>\n",
       "      <th>INF_A</th>\n",
       "      <th>BYAMAGATA</th>\n",
       "      <th>...</th>\n",
       "      <th>Country_New Zealand</th>\n",
       "      <th>Country_Papua New Guinea</th>\n",
       "      <th>Country_Philippines</th>\n",
       "      <th>Country_Republic of Korea</th>\n",
       "      <th>Country_Singapore</th>\n",
       "      <th>Country_Viet Nam</th>\n",
       "      <th>WHOREGION_Western Pacific Region of WHO</th>\n",
       "      <th>FLUREGION_Eastern Asia</th>\n",
       "      <th>FLUREGION_Oceania Melanesia Polynesia</th>\n",
       "      <th>FLUREGION_South-East Asia</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>EDATE</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2000-01-09</th>\n",
       "      <td>2000</td>\n",
       "      <td>1</td>\n",
       "      <td>2000-01-03</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2000-01-16</th>\n",
       "      <td>2000</td>\n",
       "      <td>2</td>\n",
       "      <td>2000-01-10</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2 rows × 34 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            Year  Week      SDATE  AH1  AH1N12009  AH3  AH5  ANOTSUBTYPED  \\\n",
       "EDATE                                                                       \n",
       "2000-01-09  2000     1 2000-01-03  0.0        0.0  1.0  0.0           0.0   \n",
       "2000-01-16  2000     2 2000-01-10  0.0        0.0  0.0  0.0           1.0   \n",
       "\n",
       "            INF_A  BYAMAGATA  ...  Country_New Zealand  \\\n",
       "EDATE                         ...                        \n",
       "2000-01-09    1.0        0.0  ...                    0   \n",
       "2000-01-16    1.0        0.0  ...                    0   \n",
       "\n",
       "            Country_Papua New Guinea  Country_Philippines  \\\n",
       "EDATE                                                       \n",
       "2000-01-09                         0                    0   \n",
       "2000-01-16                         0                    0   \n",
       "\n",
       "            Country_Republic of Korea  Country_Singapore  Country_Viet Nam  \\\n",
       "EDATE                                                                        \n",
       "2000-01-09                          0                  0                 0   \n",
       "2000-01-16                          0                  0                 0   \n",
       "\n",
       "            WHOREGION_Western Pacific Region of WHO  FLUREGION_Eastern Asia  \\\n",
       "EDATE                                                                         \n",
       "2000-01-09                                        1                       0   \n",
       "2000-01-16                                        1                       0   \n",
       "\n",
       "            FLUREGION_Oceania Melanesia Polynesia  FLUREGION_South-East Asia  \n",
       "EDATE                                                                         \n",
       "2000-01-09                                      1                          0  \n",
       "2000-01-16                                      1                          0  \n",
       "\n",
       "[2 rows x 34 columns]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "cat_data.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "7b941101",
   "metadata": {
    "_cell_guid": "f1051114-6fb1-4586-aab2-94dd7926c41b",
    "_uuid": "65719102-12cd-4b80-96f6-7b76b0445f7b",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:24.679801Z",
     "iopub.status.busy": "2022-05-01T20:48:24.679265Z",
     "iopub.status.idle": "2022-05-01T20:48:24.683612Z",
     "shell.execute_reply": "2022-05-01T20:48:24.683026Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.031586,
     "end_time": "2022-05-01T20:48:24.685769",
     "exception": false,
     "start_time": "2022-05-01T20:48:24.654183",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Prophet 0.7.1\n"
     ]
    }
   ],
   "source": [
    "import fbprophet\n",
    "# print version number\n",
    "print('Prophet %s' % fbprophet.__version__)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "133ab0c3",
   "metadata": {
    "_cell_guid": "6034ca3d-ac7f-4046-b70b-347ad0a6138a",
    "_uuid": "968cd5b3-30f4-4d42-b707-21a28658a2a6",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:24.737501Z",
     "iopub.status.busy": "2022-05-01T20:48:24.737207Z",
     "iopub.status.idle": "2022-05-01T20:48:27.409021Z",
     "shell.execute_reply": "2022-05-01T20:48:27.408180Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 2.699943,
     "end_time": "2022-05-01T20:48:27.411545",
     "exception": false,
     "start_time": "2022-05-01T20:48:24.711602",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "outbreak=pickle.load(open('../input/flu-spook-models/outbreak.sav', 'rb'))\n",
    "model=pickle.load(open('../input/flu-spook-models/prophet.sav', 'rb'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "988db7af",
   "metadata": {
    "_cell_guid": "0b8b9c2b-2184-4aa4-89b2-c8d9e1511121",
    "_uuid": "aa81ad66-9830-4309-98a5-3144d242e971",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:27.466597Z",
     "iopub.status.busy": "2022-05-01T20:48:27.466321Z",
     "iopub.status.idle": "2022-05-01T20:48:27.503725Z",
     "shell.execute_reply": "2022-05-01T20:48:27.502975Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.065993,
     "end_time": "2022-05-01T20:48:27.506016",
     "exception": false,
     "start_time": "2022-05-01T20:48:27.440023",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "prophet_df=cat_data.reset_index()\n",
    "prophet_df.rename(columns = {'EDATE':'ds', 'ALL_INF':'y'}, inplace = True)\n",
    "\n",
    "\n",
    "# prepare expected column names\n",
    "df= prophet_df\n",
    "\n",
    "#df= [ds, y]\n",
    "#df.columns = ['ds', 'y']\n",
    "df['ds']= to_datetime(df['ds'])\n",
    "\n",
    "#split data\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "x_train, x_test= train_test_split(df, test_size=0.3)\n",
    "x_train.sort_values(by='ds', axis=0, ascending=True, inplace=True)\n",
    "x_test.sort_values(by='ds', axis=0, ascending=True, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "7502fd8f",
   "metadata": {
    "_cell_guid": "dcb019ef-5f07-452a-96c7-7508779139e4",
    "_uuid": "6a509ca5-c322-4b31-90b1-5ecc56433d5c",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:27.555957Z",
     "iopub.status.busy": "2022-05-01T20:48:27.555683Z",
     "iopub.status.idle": "2022-05-01T20:48:27.577746Z",
     "shell.execute_reply": "2022-05-01T20:48:27.576822Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.049305,
     "end_time": "2022-05-01T20:48:27.579698",
     "exception": false,
     "start_time": "2022-05-01T20:48:27.530393",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ds</th>\n",
       "      <th>Year</th>\n",
       "      <th>Week</th>\n",
       "      <th>SDATE</th>\n",
       "      <th>AH1</th>\n",
       "      <th>AH1N12009</th>\n",
       "      <th>AH3</th>\n",
       "      <th>AH5</th>\n",
       "      <th>ANOTSUBTYPED</th>\n",
       "      <th>INF_A</th>\n",
       "      <th>...</th>\n",
       "      <th>Country_New Zealand</th>\n",
       "      <th>Country_Papua New Guinea</th>\n",
       "      <th>Country_Philippines</th>\n",
       "      <th>Country_Republic of Korea</th>\n",
       "      <th>Country_Singapore</th>\n",
       "      <th>Country_Viet Nam</th>\n",
       "      <th>WHOREGION_Western Pacific Region of WHO</th>\n",
       "      <th>FLUREGION_Eastern Asia</th>\n",
       "      <th>FLUREGION_Oceania Melanesia Polynesia</th>\n",
       "      <th>FLUREGION_South-East Asia</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2000-01-09</td>\n",
       "      <td>2000</td>\n",
       "      <td>1</td>\n",
       "      <td>2000-01-03</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2000-01-16</td>\n",
       "      <td>2000</td>\n",
       "      <td>2</td>\n",
       "      <td>2000-01-10</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>0.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>...</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>2 rows × 35 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "          ds  Year  Week      SDATE  AH1  AH1N12009  AH3  AH5  ANOTSUBTYPED  \\\n",
       "0 2000-01-09  2000     1 2000-01-03  0.0        0.0  1.0  0.0           0.0   \n",
       "1 2000-01-16  2000     2 2000-01-10  0.0        0.0  0.0  0.0           1.0   \n",
       "\n",
       "   INF_A  ...  Country_New Zealand  Country_Papua New Guinea  \\\n",
       "0    1.0  ...                    0                         0   \n",
       "1    1.0  ...                    0                         0   \n",
       "\n",
       "   Country_Philippines  Country_Republic of Korea  Country_Singapore  \\\n",
       "0                    0                          0                  0   \n",
       "1                    0                          0                  0   \n",
       "\n",
       "   Country_Viet Nam  WHOREGION_Western Pacific Region of WHO  \\\n",
       "0                 0                                        1   \n",
       "1                 0                                        1   \n",
       "\n",
       "   FLUREGION_Eastern Asia  FLUREGION_Oceania Melanesia Polynesia  \\\n",
       "0                       0                                      1   \n",
       "1                       0                                      1   \n",
       "\n",
       "   FLUREGION_South-East Asia  \n",
       "0                          0  \n",
       "1                          0  \n",
       "\n",
       "[2 rows x 35 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "prophet_df.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "6e9be097",
   "metadata": {
    "_cell_guid": "36f04196-9b73-4351-a9b6-9bf6386fe092",
    "_uuid": "bb14ccc7-b2d7-4557-9872-6a1898b3126d",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:27.633765Z",
     "iopub.status.busy": "2022-05-01T20:48:27.632914Z",
     "iopub.status.idle": "2022-05-01T20:48:33.966435Z",
     "shell.execute_reply": "2022-05-01T20:48:33.965572Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 6.361874,
     "end_time": "2022-05-01T20:48:33.968460",
     "exception": false,
     "start_time": "2022-05-01T20:48:27.606586",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAsgAAAGoCAYAAABbtxOxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAACJaElEQVR4nO3dd5wTZf4H8E+S3Sy9Lb1IcQHpIDUIElgR260NBX8qnKAgFkTvFKV4FhTFBmKBVVTW84Q7PAEbootzFoayFEWwoIJ0hIVF2m7a/P6YTXaSTJJJdiZtP+/Xy5ckO5l5JjNJvvPM9/k+JkmSJBAREREREQDAnOgGEBERERElEwbIREREREQKDJCJiIiIiBQYIBMRERERKTBAJiIiIiJSyEh0A4zQsGFDtGnTJtHNSAtOpxOZmZmJbgZpwGOVGnicUgePVergsUodyXasdu/ejaNHjwY9n5YBcps2bVBUVJToZqSFAwcOoHnz5oluBmnAY5UaeJxSB49V6uCxSh3Jdqz69Omj+jxTLIiIiIiIFBggExEREREpMEAmIiIiIlJggExEREREpMAAmYiIiIhIgQEyEREREZECA2QiIiIiIgUGyERERERECgyQiYiIiIgUGCATERERESkwQCYiIiIiUmCATERERESkwACZiIiIiEiBATIRERERkQIDZCIiIiKNRFHE7NmzIYpioptCBspIdAOIiIiIUoEoisjNzYXD4YDVakVhYSFsNluim0UGYA8yERERkQaCIMDhcMDtdsPhcEAQhEQ3iQzCAJmIiIhIA7vdDqvVCovFAqvVCrvdnugmkUGYYkFERESkgc1mQ2FhIQRBgN1uZ3pFGmOATERERKSRzWZjYFwFMMWCiIiIiEiBATIRERERkQIDZCIiIiIiBQbIREREREQKDJCJiIiIiBQYIBMRERERKTBAJiIiIiJSYIBMRERERKTAAJmIiIiISIEBMhERERGRgqEB8gsvvIAuXbqga9euuOGGG1BaWopdu3ahf//+yMnJwahRo+BwOAAAZWVlGDVqFHJyctC/f3/s3r3bt57Zs2cjJycHHTt2xKeffmpkk4mIiIioijMsQN6/fz9efPFFFBUV4fvvv4fb7caSJUswdepU3Hvvvfjll19Qv359LFq0CACwaNEi1K9fH7/88gvuvfdeTJ06FQCwY8cOLFmyBNu3b8eqVatwxx13wO12G9VsIiIiIqriDO1BdrlcOHv2LFwuF86cOYNmzZphzZo1GDlyJABg7NixWL58OQBgxYoVGDt2LABg5MiRKCwshCRJWLFiBUaPHo2srCy0bdsWOTk52LBhg5HNJiIiIqIqLMOoFbdo0QJ///vfcc4556B69eq4+OKL0bt3b9SrVw8ZGfJmW7Zsif379wOQe5xbtWolNyojA3Xr1kVxcTH279+PAQMG+NarfI1Sfn4+8vPzAQCHDh3CgQMHjNq1KuXIkSOJbgJpxGOVGnicUgePVergsUodqXKsDAuQjx8/jhUrVmDXrl2oV68errvuOqxatcqozWHChAmYMGECAKBPnz5o3ry5Yduqavhepg4eq9TA45Q6eKxSB49V6kiFY2VYisXnn3+Otm3bolGjRsjMzMQ111yDb775BiUlJXC5XACAffv2oUWLFgDkHue9e/cCkFMzTpw4gezsbL/nA19DRERERKQ3wwLkc845B+vWrcOZM2cgSRIKCwvRuXNnDB06FMuWLQMALF68GFdeeSUAIC8vD4sXLwYALFu2DMOGDYPJZEJeXh6WLFmCsrIy7Nq1Czt37kS/fv2MajYRERERVXGGpVj0798fI0eOxPnnn4+MjAz06tULEyZMwOWXX47Ro0djxowZ6NWrF8aPHw8AGD9+PG6++Wbk5OSgQYMGWLJkCQCgS5cuuP7669G5c2dkZGTg5ZdfhsViMarZRERERFTFmSRJkhLdCL316dMHRUVFiW5GWjhw4EBK5AoRj1Wq4HFKHTxWqSPex0oURQiCALvdDpvNFrftpoNk+1yFihk5kx4RERGltKKiIsyePRuiKBq+rZVrvsbAZUcx44WFyM3Njcs2Kf4YIBMREVHKEkURo0aNwsyZM+MSsOYLOwAAni7D4XA4IAiCodujxGCATERERClLEAQ4nU643e64BKw5OTkAAJPJBKvVCrvdbuj2KDEYIBMREVHKstvtyMzMhMViiUvA2qZNGwBAt/P7orCwkDnIacqwKhZERERERrPZbFi6dCm2b98e10FzXXqcD5utd1y2RfHHAJmIiIhSWp8+fZCXl5foZlAaYYoFEREREZECA2QiIiIiIgUGyERERERECgyQiYiIiIgUGCATERERESkwQCYiIiIiUmCATERERESkwACZiIiIiEiBATIRkU5EUcTs2bMhimKim0JE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8sfq+PHjWLFiBXbt2oUDBw7g9OnT+Oc//2lkk6usaI/VF198gUWLFuHpp5/WvJ54YkRTBTmdTlx77bW48cYbcc011wAAmjRpgoMHDwKQg97GjRsDkK++9+7d63vtvn370KJFCwDAn3/+icsvvxxPPPEEBgwYEOe9qBr0OFYtW7ZEz5490a5dO2RkZOCqq67yG8BH+ojmWIUS7vNG+tDjOH3zzTdYuXIl2rRpg9GjR2PNmjW46aabDG97VaPHsfr888/Rtm1bNGrUCJmZmbjmmmuwdu1aw9te1UR7rL777jvceuutWLFiBbKzs8OuJ1EYIFcxkiRh/Pjx6NSpE+677z7f83l5eVi8eDEAYPHixbjyyit9zxcUFECSJKxbtw5169ZFs2bN4HA4cPXVV2PMmDEYOXJkQvYl3el1rPr27YuSkhJfjviaNWvQuXPn+O9QGov2WIXSt29f7Ny5E7t27YLD4cCSJUuQl5dnaNurEr2O0+zZs7Fv3z7s3r0bS5YswbBhw9grqTO9jtU555yDdevW4cyZM5AkCYWFhejUqZOhba9qoj1We/bswTXXXIO3334bHTp0iLiehEnU6EBKjK+++koCIHXr1k3q0aOH1KNHD+mjjz6Sjh49Kg0bNkzKycmRcnNzpeLiYkmSJMnj8Uh33HGH1K5dO6lr167Sxo0bJUmSpLffflvKyMjwraNHjx7Sli1bErhn6UevYyVJkrR69WqpW7duUteuXaWxY8dKZWVlidqttBTtsTp48KDUokULqXbt2lLdunWlFi1aSCdOnJAkSa5G0r59e6ldu3bSrFmzErlbaUfP4+T1xRdfsIqFAfQ8Vg8//LDUsWNHqUuXLtJNN90klZaWJnLX0k60x2r8+PFSvXr1fMv27t077HoShVNNExEREREpMMWCiIiIiEiBATIRERERkQIDZCIiIiIiBQbIREREREQKDJCJiIiIiBQYIBMRpblHHnkEzz77bKKbQUSUMhggExEREREpMEAmIkpDTzzxBDp06IBBgwbhp59+AgC8+OKL6Ny5M7p3747Ro0cnuIVERMkrI9ENICIifW3atAlLlizB1q1b4XK5cP7556N379546qmnsGvXLmRlZaGkpCTRzSQiSlrsQSYiSjNfffUVrr76atSoUQN16tRBXl4eAKB79+648cYb8c9//hMZGewfISIKhQEyEVEV8dFHH+HOO+/E5s2b0bdvX7hcrkQ3iYgoKTFAJiJKMxdeeCGWL1+Os2fP4uTJk/jggw/g8Xiwd+9eDB06FE8//TROnDiBU6dOJbqpRERJiffYiIjSzPnnn49Ro0ahR48eaNy4Mfr27QuTyYSbbroJJ06cgCRJmDx5MurVq5fophIRJSWTJElSohtBRERERJQsmGJBRERERKTAAJmIiIiISIEBMhERERGRAgNkIiIiIiIFBshERERERAoMkImIiIiIFBggExEREREp/D+XGXxASYOXjgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAsgAAAGoCAYAAABbtxOxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/YYfK9AAAACXBIWXMAAAsTAAALEwEAmpwYAACJaElEQVR4nO3dd5wTZf4H8E+S3Sy9Lb1IcQHpIDUIElgR260NBX8qnKAgFkTvFKV4FhTFBmKBVVTW84Q7PAEbootzFoayFEWwoIJ0hIVF2m7a/P6YTXaSTJJJdiZtP+/Xy5ckO5l5JjNJvvPM9/k+JkmSJBAREREREQDAnOgGEBERERElEwbIREREREQKDJCJiIiIiBQYIBMRERERKTBAJiIiIiJSyEh0A4zQsGFDtGnTJtHNSAtOpxOZmZmJbgZpwGOVGnicUgePVergsUodyXasdu/ejaNHjwY9n5YBcps2bVBUVJToZqSFAwcOoHnz5oluBmnAY5UaeJxSB49V6uCxSh3Jdqz69Omj+jxTLIiIiIiIFBggExEREREpMEAmIiIiIlJggExEREREpMAAmYiIiIhIgQEyEREREZECA2QiIiIiIgUGyERERERECgyQiYiIiIgUGCATERERESkwQCYiIiIiUmCATERERESkwACZiIiIiEiBATIRERERkQIDZCIiIiKNRFHE7NmzIYpioptCBspIdAOIiIiIUoEoisjNzYXD4YDVakVhYSFsNluim0UGYA8yERERkQaCIMDhcMDtdsPhcEAQhEQ3iQzCAJmIiIhIA7vdDqvVCovFAqvVCrvdnugmkUGYYkFERESkgc1mQ2FhIQRBgN1uZ3pFGmOATERERKSRzWZjYFwFMMWCiIiIiEiBATIRERERkQIDZCIiIiIiBQbIREREREQKDJCJiIiIiBQYIBMRERERKTBAJiIiIiJSYIBMRERERKTAAJmIiIiISIEBMhERERGRgqEB8gsvvIAuXbqga9euuOGGG1BaWopdu3ahf//+yMnJwahRo+BwOAAAZWVlGDVqFHJyctC/f3/s3r3bt57Zs2cjJycHHTt2xKeffmpkk4mIiIioijMsQN6/fz9efPFFFBUV4fvvv4fb7caSJUswdepU3Hvvvfjll19Qv359LFq0CACwaNEi1K9fH7/88gvuvfdeTJ06FQCwY8cOLFmyBNu3b8eqVatwxx13wO12G9VsIiIiIqriDO1BdrlcOHv2LFwuF86cOYNmzZphzZo1GDlyJABg7NixWL58OQBgxYoVGDt2LABg5MiRKCwshCRJWLFiBUaPHo2srCy0bdsWOTk52LBhg5HNJiIiIqIqLMOoFbdo0QJ///vfcc4556B69eq4+OKL0bt3b9SrVw8ZGfJmW7Zsif379wOQe5xbtWolNyojA3Xr1kVxcTH279+PAQMG+NarfI1Sfn4+8vPzAQCHDh3CgQMHjNq1KuXIkSOJbgJpxGOVGnicUgePVergsUodqXKsDAuQjx8/jhUrVmDXrl2oV68errvuOqxatcqozWHChAmYMGECAKBPnz5o3ry5Yduqavhepg4eq9TA45Q6eKxSB49V6kiFY2VYisXnn3+Otm3bolGjRsjMzMQ111yDb775BiUlJXC5XACAffv2oUWLFgDkHue9e/cCkFMzTpw4gezsbL/nA19DRERERKQ3wwLkc845B+vWrcOZM2cgSRIKCwvRuXNnDB06FMuWLQMALF68GFdeeSUAIC8vD4sXLwYALFu2DMOGDYPJZEJeXh6WLFmCsrIy7Nq1Czt37kS/fv2MajYRERERVXGGpVj0798fI0eOxPnnn4+MjAz06tULEyZMwOWXX47Ro0djxowZ6NWrF8aPHw8AGD9+PG6++Wbk5OSgQYMGWLJkCQCgS5cuuP7669G5c2dkZGTg5ZdfhsViMarZRERERFTFmSRJkhLdCL316dMHRUVFiW5GWjhw4EBK5AoRj1Wq4HFKHTxWqSPex0oURQiCALvdDpvNFrftpoNk+1yFihk5kx4RERGltKKiIsyePRuiKBq+rZVrvsbAZUcx44WFyM3Njcs2Kf4YIBMREVHKEkURo0aNwsyZM+MSsOYLOwAAni7D4XA4IAiCodujxGCATERERClLEAQ4nU643e64BKw5OTkAAJPJBKvVCrvdbuj2KDEYIBMREVHKstvtyMzMhMViiUvA2qZNGwBAt/P7orCwkDnIacqwKhZERERERrPZbFi6dCm2b98e10FzXXqcD5utd1y2RfHHAJmIiIhSWp8+fZCXl5foZlAaYYoFEREREZECA2QiIiIiIgUGyERERERECgyQiYiIiIgUGCATERERESkwQCYiIiIiUmCATERERESkwACZiIiIiEiBATIRkU5EUcTs2bMhimKim0JERJXAAJmISAeiKGLIlGcw7WhXDLvkCgbJREQpjAEyEZEOBEGAs8OFAABHjWwIgpDYBhERUcwYIBMR6cBut8Nkkr9SLRmZsNvtiW0QERHFjAEyEZEObDYb2rfPAQBMm/0cbDZbgltERESxYoBMRKSTmjVrAgDad+qa4JYQVT0cJEt6ykh0A4iIiIgqo6ioCKNHj4bD4YDVakVhYSHv4lClsAeZiIiIUpooinA4HHC73XA4HBwkS5XGAJmIiIhSms1mg9VqhcVigdVq5SBZqjSmWBAREVFK69OnDwoLCyEIAux2O9MrqNIYIBMREVHKs9lsDIxJN0yxICIiIiJSYIBMRERERKTAAJmIiIhIo927dwMAjvxxOLENIUMxQCYiIiLS4Ju1azHv29MAgC8++YCTkqQxBshEREREGjy1apvv3x6P29B6y5wZMLFYxYKIiIhIg2ZtcoDtZwAAZrPFsHrLoigiNzeXMwMmEHuQiYiIiDQ4p1Ur37+HXvoXw4JWQRA4M2CCMUAmIiIiilKjxk0MW7fdbufMgAnGFAsiIiKiJGKz2TgzYIIxQCYiIiJKMpwZMLGYYkFEREREpMAAmYiIiIhIgQEyEREREZECA2QiIiIiIgUGyEREOnvhy9/g8UiJbgZRlVFUVMRZ50hXrGJBRKSzTftO4O1N+zC2b6vICxNRpYiiiFGjRsHpdHLWOdINe5CJiAzgdHsS3QSiKkEQBDidTs46R7piDzIRERGlLLvdjszMTADgrHOkGwbIREQGMCW6AURVhM1mw9KlS7F9+3bOOke6YYBMREREKa1Pnz7Iy8tLdDMojTAHmYjICOxCJiJKWQyQiYiIiIgUGCATERnAxC5kIqKUxQCZiIiIiEiBATIRkQHYf0xElLoYIBMRERERKTBAJiIygIldyEREKYsBMhERERGRAgNkIiIDsAOZiCh1MUAmIiIiIlJggExEREQpTxRFzJ49G6IoJroplAYyEt0AIqK0xFF6RHFTVFSE0aNHw+FwwGq1orCwEDabLdHNohTGHmQiIiJKaaIowuFwwO12w+FwQBCERDepUtgbnnjsQSYiMgD7j4nix2azwWq1+nqQ7XZ7opsUM1EUkZuby97wBGOATERERCmtT58+KCwshCAIsNvtKR1QCoIQ1BueyvuTqhggExEZgCnIRPFls9niGkhu/3YzxByH7tu02+1p0xueypiDTERERBSl76SmyM3N1T1P2GazobCwEI8//jjTKxKIPchERAZgBzJR+jMqBSLeveEUjD3IRERERDFgCkT6YoBMRGQAE5OQidLex5+uZk9vmmKATERERBSD/gMYHKcrBshERERERAoMkImIiChliaKI+fPnJ2TWOUmSDF0/Z9RLHFaxICIyADOQiYynnHVu3rx5aVUWjTPqJRZ7kImIiCglqc06ly7Sed9SAQNkIiIiSkneWecsFkvalVxL531LBUyxICIyAKu8ERnPO+vcypUrkZeXl1YpCN59EwQBdrs9rfYtFTBAJiIiopRls9nQunVrNG/ePO7bNniMHmfUSyBDUyxKSkowcuRInHfeeejUqRNEUcSxY8cwfPhwtG/fHsOHD8fx48cByCNBJ0+ejJycHHTv3h2bN2/2rWfx4sVo37492rdvj8WLFxvZZCIiXZg4TI8o7lj1gfRiaIB8zz334JJLLsGPP/6Ib7/9Fp06dcJTTz2F3Nxc7Ny5E7m5uXjqqacAAJ988gl27tyJnTt3Ij8/H5MmTQIAHDt2DI8++ijWr1+PDRs24NFHH/UF1URERERARdWHmTNnIjc3l0EyVYphAfKJEyfw5ZdfYvz48QDk+crr1auHFStWYOzYsQCAsWPHYvny5QCAFStWYMyYMTCZTBgwYABKSkpw8OBBfPrppxg+fDgaNGiA+vXrY/jw4Vi1apVRzSYi0gVzkInii1UfSE+G5SDv2rULjRo1wi233IJvv/0WvXv3xrx583D48GE0a9YMANC0aVMcPnwYALB//360atXK9/qWLVti//79IZ8PlJ+fj/z8fADAoUOHcODAAaN2rUo5cuRIoptAGvFYJZ7T6fT9+8/jxThwIDhK5nFKHTxWqePIkSPo0qULMjMzAQCZmZno0qWL7rHAnydP+j0+dOggqmdadN1GukuVz5VhAbLL5cLmzZsxf/589O/fH/fcc48vncLLZDLBpFM3y4QJEzBhwgQAQJ8+fRKSrJ+u+F6mDh6rxMrM3AngLACgTv3skMeDxyl18Filjh49emDNmjWGVn2oU/uU3+MmTZuhVhbrHUQrFT5XhqVYtGzZEi1btkT//v0BACNHjsTmzZvRpEkTHDx4EABw8OBBNG7cGADQokUL7N271/f6ffv2oUWLFiGfJyIiIlKy2Wx46KGHWPmBKs2wALlp06Zo1aoVfvrpJwBAYWEhOnfujLy8PF8lisWLF+PKK68EAOTl5aGgoACSJGHdunWoW7cumjVrhhEjRmD16tU4fvw4jh8/jtWrV2PEiBFGNZuISBfMQSYiSl2G3heYP38+brzxRjgcDrRr1w5vvvkmPB4Prr/+eixatAitW7fGv//9bwDAZZddho8//hg5OTmoUaMG3nzzTQBAgwYNMHPmTPTt2xcA8PDDD6NBgwZGNpuIiIiIqjBDA+SePXuiqKgo6PnCwsKg50wmE15++WXV9YwbNw7jxo3TvX1EREZhBzIRUeoytA4yERERUboyeiY9ShwGyEREBtCrQg8REcUfA2QiIiIiIgUGyERERERECgyQiYgMwAQLIqLUxQCZiIiIKAYSOEovXTFAJiIykCiKmD17NkRRTHRTiIhII04gTkRkEFEUkZubC4fDAavVisLCQrRu3TrRzSKiJPfRF9/gu3Vfwm63c9rsBGEPMhGRAUwmQBAEOBwOuN1uOBwOCIKQ6GYRUZJ76+OvcMWHxzD9/U3Izc3l3acEYYBMRGQQu90Oq9UKi8UCq9UKu92e6CYRUZJbtWEbAEBq1JYX1gnEFAsiIgOYYILNZkNhYSEEQfDdKj1w4ECim0ZEOjFiJr3OnTsD60/CZDLxwjqBGCATERnIZrMxh5CINOvQvj2wfjPOPa8zCqYX8vsjQZhiQURkAM40TUSV0bZ9RwbHCcQAmYiIiIhIgQEyEZEB2IFMRJS6GCATEelAFEUcPnQ40c0gojjiPHrpiwEyEVEleScEOXBQUaGCXchERCmLATIRUSV5JwRhdxIRUXpggExEVEneCUHYa0xElB4YIBMRVZJ3QpDmzZr7njMxWiYiSlkMkImIdGCz2dCkaZNEN4OI4kgyYio9SgoMkImIDMD+YyKi1MUAmYiIiIhIgQEyEZEBONU0EVHqYoBMREREFANmIKcvBshERERERAoMkImIiIiIFBggExERVWGiKGL27NkQRTHRTSFKGgyQiYiIqihRFDFk0iOYdrQrhuVexCA5yfDiJXEyEt0AIqJ0JYoiBEGA3W6HzWZLdHOIggiCAGf//wMAODJrQBAEnqtRMHKekBPHjiE39zo4HA5YrVYUFhby2MQRe5CJiAzww7ZvMSw3FzNefAO5ubnsAaKkZLfbfbPaZGRY5ceUFI4VH4HD4YDb7YbD4YAgCIluUpXCAJmIyADbNm9EWeeL4fm/51HWqD1/3Cgp2Ww2NMxuCACY/cob7KFMIg2yG8FqtcJiscBq5cVLvDHFgojIAN3O7wvz9uNwAzDXb84fN0pamdZMoLQMnbv3THRTouZNY+rSpQvy8vIS3Rxd1W3QAIWFhUzTShAGyEREBujUrQdGjDDh49/LcPPtk/njRqQzURSRm5sLh8OBzMxMrFmzJu0+ZzabLe32KVUwxYKIyCCNGzcGALRs0zbBLSGKbOmb+SmVKy8Igi9H1+l0JiSNSTJylB4lFANkIiKDmBLdACINnA4nAGDxwhdTakCp3W735ehmZmYyjYl0xRQLIiKDsZOJklmZowxAJiS3x1ctIRVu69tsNl+ObpcuXVKizZQ6GCATERnExC5kSgFZ1iycLPXAbDGnXLUEb47ugQMHEt0USjNMsSAiMoiJSRaUAjKtmQCAMRMnczIKonLsQSYiMhgH8lAqGHXLBNg6NUl0M1LK8bNONKyVlehmkAHYg0xEZBBvigXDY6L0sGfvXr/HHZ76IkEtIaMxQCYiMghzkInShyiKeG37maDnT5a6EtAaMhoDZCIigzHDgij1cbr4qoUBMhGRQdiBTJQ+Uqm6B1UeA2QiIoOxA5ko9bG6R9XCAJmIyCAm3yg9hshE8SKKImbPnh23GQE51iA9scwbEZFB+LtJFF+iKCI3NxcOhwNWq5V1nSlm7EEmIjIY+4+J4kMQBDgcDrjdbt+02USxYIBMRGQQ1kEmii+73Q6r1QqLxRK3abN5pyg9McWCiMggnGo6tRUVFWH79u2w2+28TZ8ibDYbCgsLIQgCjxtVCgNkIiKDcYxe6hFFEaNGjYLT6WQua4qx2Ww8VlRpTLEgIjIIR7enLkEQ4HQ6q0Quq9PhBADs+G5rYhtClEQYIBMRGUxiFnLKsdvtyMzMjGsuayKIooijpR4AwEN3jItbabR0wgvh9MQUCyIig/h+NxkfpxybzYalS5emfQ6y3DPeFQDgcsk95em6r0TRYIBMRGQQE7uWUlqfPn2Ql5eX6GYYKjs7Gzgq/zsjI317yomixRQLIiKDsQOZkpEoipgyZYrv8cT7HmTvMVE5BshERAbhTNOUzLyTanidPFGSuMakMN4pSk9MsSAiMgh/NimZeSfVOFv+uFvvfgltT6qaeOc9qGFxY+yYMeyBTyPsQSYiMhg7kCkZeSfV8OrcvWfiGpPC3q49AgvX/o6hQ4eyCkgaYYBMRGQQ3nmlZMceT52065P29bKrGgbIREQGYx1kovSXzvWyqyIGyEREBjF5s5AZHxOltSYtWuGLL75gj3waYYBMRGQQplgQGUsURcyePRtFRUUJbce5HToxOE4zDJCJiAzGDmQi/YmiiIHLjmLaZjdGjRrFAXKkKwbIREQG8XYgsw4ykf58A+LO6QGn05nQAXL8iKcfBshERAbhBAJExlEOiMvMzEzoADmJV8FpJ2KAPH/+fBw/fjwebSEiSksH9+3B7NmzeQuYSEfKnN+lS5cmNAeY4XH6iRggHz58GH379sX111+PVatW8SqJiEiFKIo4fOiw33Pe/uP3VhVixrMvIzc3N+GDiYjSUZ8+fRK6/VN/nkjo9kl/EQPkWbNmYefOnRg/fjzeeusttG/fHtOmTcOvv/4aj/YRESU9URSRm5uLAwcP+D3vzbDwnGeH56+vwuFwsBeZKA3t2PYtP9tpRlMOsslkQtOmTdG0aVNkZGTg+PHjGDlyJB544AGj20dElPQEQYDD4Yh4n9VqtbIUFFEakiQJjzzyCIPkNBIxQJ43bx569+6NBx54ABdccAG2bduGV199FZs2bcJ7770XjzYSESU1u90Oq9VakVNRzhTwRGFhYcJvBVN0vHV2GfhQJJ9//jlyc3N5rqSJiAHysWPH8N///heffvoprrvuOmRmZsovNJvx4YcfGt5AIqJkZ7PZUFhYiObNmoddThAE5iCnkKKiIthv+RtmvP5fBj4UgQkejwcOhyOh5eZIPxED5EcffRStW7dW/VunTp10bxARUSqy2Wxo0rSJ33OBVd5mzpzJCQ1SiCiKcFz+EDxXPczAh8Iymc2wWCywWq0JLTdH+jG8DrLb7UavXr1wxRVXAAB27dqF/v37IycnB6NGjZLz9gCUlZVh1KhRyMnJQf/+/bF7927fOmbPno2cnBx07NgRn376qdFNJiLSRWCA7Ha7Ez6hAWkjiiL279/ve8zAh8Lp2KUbHn/8cRQWFnKcQZowPECeN2+eX0/z1KlTce+99+KXX35B/fr1sWjRIgDAokWLUL9+ffzyyy+49957MXXqVADAjh07sGTJEmzfvh2rVq3CHXfcAbfbbXSziYh0Z7FYEj6hAUXmrUryr3/9y/ccAx8Kp2btOnjooYd4jqQRQwPkffv24aOPPsKtt94KQB7luWbNGowcORIAMHbsWCxfvhwAsGLFCowdOxYAMHLkSBQWFkKSJKxYsQKjR49GVlYW2rZti5ycHGzYsMHIZhMR6SJwHr3HH3884RMaUGTeqiTKzpiqcMyWvpnP9J8YnTr5Z6KbQDrLMHLlU6ZMwZw5c3Dy5EkAQHFxMerVq4eMDHmzLVu29N3C2r9/P1q1aiU3KiMDdevWRXFxMfbv348BAwb41ql8jVJ+fj7y8/MBAIcOHcKBAweClqHoHTlyJNFNII14rBLP6XT6/v3nsaM4deqs39/Hjh2LI0eO8PspyXXp0sU3IN0bIleFY7Z4wTwsmf8kli5dmnLVVhL9/Xfi+HHdzhHv7MXOsrK0PO8Sfay0MixA/vDDD9G4cWP07t07Lvl2EyZMwIQJEwDIM+o0bx5+NDlpx/cydfBYJVZm5k4AclBcp0FD1D5VAuCQ7+/e48PjlNzy8vKwZs0arFy5Ek/Jw2TS/JhtAgBIHglOpxPbt29HXl5egtukldz2Ro0axekYbVJ9tk69+rptv/5hCcAuZGZlpe15lwr7ZViA/M0332DlypX4+OOPUVpaij///BP33HMPSkpK4HK5kJGRgX379qFFixYAgBYtWmDv3r1o2bIlXC4XTpw4gezsbN/zXsrXEBEls8AUC0odNpsNrVu3xlPPqQdE6chsMXMwYoxq1q6d6CaQzgzLQZ49ezb27duH3bt3Y8mSJRg2bBjeeecdDB06FMuWLQMALF68GFdeeSUA+Yp98eLFAIBly5Zh2LBhMJlMyMvLw5IlS1BWVoZdu3Zh586d6Nevn1HNJiIiqpLGTJycFIMRU3FyFinCLJqUegzNQVbz9NNPY/To0ZgxYwZ69eqF8ePHAwDGjx+Pm2++GTk5OWjQoAGWLFkCQM4Fu/7669G5c2dkZGTg5ZdfhsViiXeziYiiFljmjSiZjbplAmydmkRe0ECiKGLYX0bCYclCVgqVTWN8nH7iEiDb7XbfLZt27dqpVqGoVq0a/vOf/6i+fvr06Zg+fbqRTSQi0l3gVNNEFJ4gCCgduwAA4Jh3NQRBSIkAmdKP4XWQiYiIiLRQ5j9nplA+NFMs0g8DZCIigzDFgig6yt7iZSs/SaHeY0bI6YYBMhGRQRgfE8WuT/8BkRdKEuxBTj8MkImIiIiIFBggExEZxMQcC4pCKpY3Ixk7kNNP3Mu8ERERkT9RFDF06FA4HA5YrVZ88cUXKZR/S0yxSD/sQSYiMsg+xSygROEUFBSgrKwMkiShrKwMBQUFiW5Swj0w5e6U6U2X2IecdhggExEZ4Idt3+K170oS3QyilKIMiAveeA1Dhw5NmSCZ0gsDZCIiA2zbvBHIsCa6GZQixowZA6vVCpPJBKvVijFjxiS6SQkhCILfY4fDEfQcUTwwB5mIyADdzu8LbHQkuhmUImw2GwRBgCAIsNvtVTb/2G63A8uO+h5bk2iykHA92cxBTj/sQSYiMkCnbj0S3QSqBFEUMX/+/Lhu02az4aGHHqqywTHgP1HImHG3Jc1gRVEUkZubm+hmUByxB5mIiEjBGww5HA7gnvcT3Zwqa87c+WhSOyvq14miqHtPvCAI8vkQAjuQ0w8DZCIiA7AEcuryBkNutzvRTaEoKS9urFYrCgsLdQmS7XY7rFYrzob4u8Qci7TDFAsiIiIFbzBksVgS3RSKkvLiRs8BfjabDYWFhSH/zvA4/TBAJiIiUvAGQ/fff3+im0JRUl7c6D3ALxlyoSl+mGJBREQUwGazoXXr1njquU2JbgpFwXtxE/dqIOxCTjsMkImIiCht2Gy2uPf2Mj5OP0yxICIiIqoETjWdfhggExEZgmUsiIhSFQNkIqI4yc/Px/z588POyEVEqYdV3tIPA2QiojiZOHEi5syZg9zcXAbJ5EcURcyePZvnRYpifJx+GCATEcWRx+PRtT4rpT5RFDFonoBphzvy4okoSTBAJiKKI7PZrHt9VkptgiDA06IrYMnkxVOqYhdy2mGZNyIiA6hNNb1w4ULs2rULeXl5nHSAfOx2O7DsKAAgkxdPKYlVLNIPA2QiojiZMGECDhw4gObNmye6KZREbDYbsOwDAMD7H67ixVMK4iA97YqKirB9+/b4TuQSAwbIRESVJIoiBEHAaVePRDeFUlzf/gMS3YS04P1MJnsQVtWIooirC7ZC+ukrVHv8cRQWFibt8WEOMhFRJVz36mcYuOwoZjz8D+zc+Uuim0MpbsM6VrOoLFEUYR87BTPy/xO3QY/sQNZGEAR4WveCdPHkpM+3Zw8yEVElfPDraQAWeMwZgORJdHOSAnvvYnfNXy6F0+GA1WpN6t61ZCYIAhx/mQEAcMy7GoIgGP4+MkDWpqftQuCDYwCQ9IOV2YNMRFQJFovcz2C2WGAyVXylqg3SqwpEUURubi5mzpzJkmUxcDoccLvdhvauSZKEmZ/8iB2HThqy/kRTBl3JHoRVNXN2VHwxJvsFIANkIqJKsFgsAIDxd/0N7dvnJLg1iScIAhxxCPLi7e2ivXHZTqbVCovFYmhgd6LUhVmf78TA+V8bsv5EUwZdcQvC2IWsyf4Tpb5/J3NwDDBAJiLSxY0T7kLNmjUT3YyEs9vtsMYhyIu3Me9uhcdjfBT03gef4PE4DV5yxWF/Ei1eQRjLvGmTSnfWmINMRES6sdlsKCwsZA5yjPr0G4DLcocYug1zeZDC0mT64XupTQrFxwyQiYhIXzabLS0DY1EU8eWX/0v5wN9UHqaw15PizZRCXcgMkImIiDQYevcsuLevQZbFuBSIeISsJvYg645vpTYpFB8zB5mIyAimlLqZSFo4h06Cp+91KT/40HtmMqjTEd9MTVLpW5EBMhGRAZa+9Vqim0BGqFEXGRkZKT340MQIWXdMV9FGmWKR7CUgGSATERlg8cKXEt0EMoIEXHrppYblIEtxyHvwBikM6ijezp454/t3stdJZ4BMRGQAye0Oek4URcyfPz+pfxQoEglNmzZNdCMqJZk7kFP1s8F8bm3OnD7t+3eypyoxQCYiipOh196EOYuWJH3PCYVmNpkxZswYw9Yfzzgr2YI6URQx9PpxvsdF69clsDXRSbK3MmnVqlVRKz7Z66QzQCYiMoLKcO2yG+bCc/OLSd9zQqENufiSlC7x9skPh3H/BzsAJF9QJwgCyq6f43u89usvE9gaMoJyMqVkn2qaZd6IiAyQZc1CWYi/JXvPCYXWsFGTRDehUi57fUPFgyTrQrbb7cCyo77HAwddmLjGRCm53snkdeZMRYpFMgfHAHuQiYgM8dQrr4f826erP0v6HwdSV3zksKHrj2fMmmxBXeBnok//AQlqSQyS7GIjGYmiiJ0lbr/HyYwBMhGRATp16xnybwMYHKesI4cOJroJuvFIUtIHKamC4XFkgWllyZ5mxgCZiIh0J4oiZs+enXYBWONmzQ1df3xLr5mQm5sbx+1RVRaYVpbsaWYMkImIDBBuxqh0vhsriiImTZqEC+94HDNeKki7ih2NGqd2DnIgh8Ph+/eO77am5UVNPOj5mf55504AwIljx/RbaRIITKFJ9jQzDtIjIiJdiKKI3NxclJaWQrp3BQDAMe9qCIKQ9D+GWqXSVLlaWK1WnC3/90N3jIP7xGFYrdakrzCQbCTI578gCLDb7TG/d6IoYtasWcDwe1Akfg1RbMDjkCDsQSYiirN0ncFMEAQ4HA6/2eDSrmKHwRFy0fr1ce3FLSws9P3b6XLA7XbrVoYwXdNs1DgdDuTm5mLmzJmVumsiCAJcLhcAQPK4kz5PN52xB5mIiHRht9thtVrhcDjgHauebj2RJoMj5NFXXQanwxG3XlybzQYs+wAAkJlhhdti0eWixns3wRHHfUkkp9Mhn/eKC4xY9tdutyPj3UI4AZjMlvS6uEwx7EEmIoqzdM1BttlsKCwsxOOPP+73XDpRmf9FV06Hvr240Zj9yht4/PHHdQlmvXcTKrMvLz43J2V6nzMyrbBarbBU8gLDZrNhxowZAIA+tkFp9/lJJQyQiYhINzabDQ899FCim2EYo3OQM3UIsmLVuXtPPPTQQ7oEZd67CZXZlydP9kyZQZ4ZmZm+i8PKXmB0aN8eAFC3QQO9mpeUkj39hikWREQG+OH7rSH/lqYdyFWC0T3I777/MX7YLFZqoFcysNlsmDt3Lt577z1ce+21Me9LZdIV4s1ms6VEO5PFtE0uVH88N2nTbxggExEZYOqkW4ExLye6GaQ7YyPk3v3646oRdkO3EQ+iKGLKlClwOBz46quv0K1bt5iCoMwUGeSZrmlThmrdM6kvgJhiQURkAIfLmegmkAGMTrFIlwoneuQgA8CS5R8nTfAkhYmC0+W4xVsyV7lhgExEZABrRmbIv4X7oaXkZk63QsgG0SMHGZB71FMBP9KxSdb0CoApFkREhnj61dcxRSxLdDNIZyaDk5DTJdDyVjSp7MQZySRdjk0ySebzggEyEZEBunTrBYjrVP/GH1qqCtJt0Bo/tlULUyyIiOLs2TlPJ3V5Iwrtu6L1PHYUhBe96YcBMhFRnD3+6D9Spr5rZaXbPm5a97Xux065LsZZyYtjByon1b4LGCATEcVZomZKixflD2HaXQhIHl2PnSiKGHrtTb7Hmzeu12W9pL9w4TFD5/BEUcSwK65JdDOiwgCZiMgA4co+JWqmtHhRBo/pdiFgMpl0PXaCIKDshrm+x+LXX+qyXoov9i6HJwgCSq+YnuhmRIUBMhGRAcL9Xs74x6NJXd6ospTBY7pdCPQZMEjXYxf43gy44EJd1pssRFFM6JTCem473Gea4XF4drsdqF470c2ICgNkIiIjhKkG9rf7p6ZtcAz4l25KtwuBXv31rcwQuK7z+/bXFFQmOvDUQhRF5ObmYubMmQlLtZnxQr5u2+ZkILGz2WxomN0w0c2ICsu8EREZIHxvU9X5oU2n4Bgwfia9TRvXYcw1V8DhcMBqtapeYHgDz3DLJAO12fTi3U5P+wvgWL8kaaczrkoyrZlAaerUhmcPMhGRAapSEFyVGD1RyPpvvoo4RbNe0zgbTa/Z9CrDZDbrtu2wF738uKcd9iATEcXZ+nXrUCR+nTYzjJF++g0cDKvV6usdVgvsvIFnuGWSQTLMpnd+/wswf84kXbYdvooFI+R0wwCZiMgA4XqU/nLJcF9w88UXXzBITiEGdyCjV59+EYPKZAg8tUr0bHo9+vaHzdZTl3WxUkXVwgCZiCjOysrKfP8vKChI6gCH/BmdgyxBW1CZ6MCT/DF2Tj/MQSYiMgJ/MNOSSecQObC6gofnTdJimbeqhQEyEZEBtOQkWiwWjBkzJg6tIb3omWIhiiLsN93l9xxzWZMXj0zVwgCZiMgA4X5MzWYzMjIy8Morr/A2eYrRM0AWBAGOqx7xe86TBl3IqVCjWXflh+3Cl7+B6W8fJLYtKSSZzxXmIBMRGSDc7djpDz+KSy/OZXCc5NQGZemZYmG324FlR/23qdvaEyNVajTHQktt869+OwYA2FV8Bm2za8SjWSltyJAhcLvdyMrKSrpzhT3IRESGCB1ITbn/gaT6ISB1avGQnj3IqudAikfIgiCgrKwMbrcbZWVlUdVodrk9xjVMB+HSXwL/4vQk974kC2f7wfB4PCgtLUVBQUGim+PHsAB57969GDp0KDp37owuXbpg3rx5AIBjx45h+PDhaN++PYYPH47jx48DkK/UJ0+ejJycHHTv3h2bN2/2rWvx4sVo37492rdvj8WLFxvVZCIiIt9t36KiTUF/M7qKhVuS0GDGKmzdf8LgLRkjOzsbnvLg0OPxIDs7W/Nr/7vtkFHNomR1yRSgSQ4kScKbb76ZVKkWhgXIGRkZeO6557Bjxw6sW7cOL7/8Mnbs2IGnnnoKubm52LlzJ3Jzc/HUU08BAD755BPs3LkTO3fuRH5+PiZNmgRADqgfffRRrF+/Hhs2bMCjjz7qC6qJiJJV2N6mFO8lTGeiKGLYFddgxqynMPqG0cELGBwhbz98EsfPOnHjO5sjL5yEiouLYTbLoYXZbEZxcbHvb5HyTT1J/sHgTHoGqVEXAOByuZJqVkjDAuRmzZrh/PPPBwDUrl0bnTp1wv79+7FixQqMHTsWADB27FgsX74cALBixQqMGTMGJpMJAwYMQElJCQ4ePIhPP/0Uw4cPR4MGDVC/fn0MHz4cq1atMqrZRES6qKq/l94gKFUJgoDSv+bDc+sbcDpdQX8/tG+PoYOKvFkGWgKuZBzgZLfbkZWVBYvFgqysLN8sf6Io4sIZb2F6wSrk5uYmVZu1Cj+TXnDJPtLGkpGZ0OnIQ4lLDvLu3buxZcsW9O/fH4cPH0azZs0AAE2bNsXhw4cBAPv370erVq18r2nZsiX2798f8nkioqQWtrcpPcNn7wCtmTNnJropMfP9QGdYkWm1Bv39PwVvYObMmYYFeVrPjfz8fAwePQHTn3kpqQJO7yx/jz/+uN+gq4KCArh6XgHpsr/D4XAkVU+hHiSPhNzcXN/jLRvXJ7A1qeXuBx8OOl+SgeFVLE6dOoVrr70Wc+fORZ06dfz+ZjKZYNJpxEN+fj7y8/MBAIcOHcKBAwd0WW9Vd+TIkUQ3gTTisUoMSZK7/E4U/wGn0+l7vuRYcaiX4I/Dh+D4M9PwtgFAUVERRFGEzWZDnz59DN3WypUr4XA44Ha7fc+l2ndx69atAciVJV555RWM/87/7x6XE5LbDYfDgZUrV5Yvr58/S+QUQrfLGfK9Kyoqwp133gn35P8CAMrmXhVzW5TbOHHsKA4ccIdZWpvWrVv77hQfOHAARUVFeOONN4C7LgMg1//u0qVL0P6ppU8ePXwI5jNZEbcZ6vuv9Mxp3c7BktLgOwpekuSBw+HwPRZWf4LBPTvFtB3v++AsK0u5z084nhCDMBs1boyxl1ScL8nC0ADZ6XTi2muvxY033ohrrrkGANCkSRMcPHgQzZo1w8GDB9G4cWMAQIsWLbB3717fa/ft24cWLVqgRYsWflea+/btU+2CnzBhAiZMmAAA6NOnD5o3b27cjlUxfC9TB49V/JlM3wLwoG52Y2RmHgFwFgBQt0EDAL+pvqZRk6ZoVCvyj35liaKIUX+9DQ5rbWTNm2d4D01eXh7mzZsnB8nlz6XmOSkPzhs2bBjw3Ra/v5gtFqD8dnBeXp4O++c/ELBWnXoAfoclIxO///47BEGA3W73O27bt2/3DYQD5IBTe1v8tye/Rn6uboOGaN68SYz7Edr27dv9LprGjRuHvLy8oOXqH5YA7PJ7rmGTpmher3qYtcttb9SoUcD+y89Xq1FTt3Ow2hkHgG/V/2gyw2q1ln/6AfvFl8a8Xe/7kJmVlaKfH3Vmy/eqz9esUz8p99OwFAtJkjB+/Hh06tQJ9913n+/5vLw8XyWKxYsX48orr/Q9X1BQAEmSsG7dOtStWxfNmjXDiBEjsHr1ahw/fhzHjx/H6tWrMWLECKOaTUSki2TIohAEAaXXzYHnxhficltbeXs9Hagdw1FjbzP0drB3k2fOnPalqwSmUHjzfL1eeumlpLo1Hchut8OqSFdJ19kjCwsLff/u1bd/AltCejAsQP7mm2/w9ttvY82aNejZsyd69uyJjz/+GA8++CA+++wztG/fHp9//jkefPBBAMBll12Gdu3aIScnB7fddhteeeUVAECDBg0wc+ZM9O3bF3379sXDDz+MBg0aGNVsIiJdJEF8LN9tqyV/X2ZmxmcAjM1mw0MPPWT4duJB7Ri2OKc1HnroIcMCUm+/8JlTp3zpKmoXN94UBgC+u6fJynvhpHys1aYN65NmIGKki95kvkih6BmWYjFo0KCQgw2UHxQvk8mEl19+WXX5cePGYdy4cbq2j4goUeLVu2yz2YBl8rS3Bf/9kD/gUVI7TnpOFKK+TXmjNWrVwimr1TcjnbIaxNCrRqNs0Digjf7bF0VRNa1Dj3UCXQEAp8pcqJWlLfwYfdVlcCbJrHzhBlAmwwUx6YtTTRMRGSDSD6YRgUg4vOWrD6MnCvGqUaMmCgsLg84RQRBQlns30Kyj7tvc8d1WzLjlal2niVZOPY173gcAtHuiEH88pi1V0hnQi86LPIoXBshERAYI19u0cf06XJd3qa6BSCTxCuzSndHvo/K0sdlsQeeF3W6H6YeNhvRYbtu0ISito7LnZUFBAUpLS/0+D0dOO8K8wl+m1QoE9KInCnuJq5a41EEmIqpqwv2Yrv36y7D5pUYwOjUgHanOhmjwG+nRkOfavn2OIdvu1rsfrFarbpM2iKKI1wu3Qrr1dcASW1nDJcs/TpoaudGkRm3ZmDy50xQb9iATERkhzI+pbdBgWBX5pdnZ2Zg9e7ah6RabN65Hu0uGGbLudKWag2z0NjX0U9asWRMo+VP3bXfu3lM1rSNWgiDANfgWoHYjoHbDmNbRu19/XHmxvVLtSIS/XvsXOJ3JkTtNsWGATERkgHCBTp9+A3yBSHZ2NiY/OR+Ous1RTeeeMmXv1c1XX4EWa4z9oVbmVacDtSNo1jFCVutdVAbl8c5TB9TTOmIhiiL27NkDmBrJT8Q4MnXThvV4e5MY1/cglGj2wOF0wMPc6ZTGFAsiIgP8d+m/Qv5NQkU5tOLiYpRd+ySki+7SPd1CuS6n09hUDlEUMSzvOkxf+pXflLvpRq/ZXwEgf3VR0HPKOsgX/v1FTDvaNammktZCFEUMu/wqLPzyx4onAwJkrekHo6+6zNCpvaMRzRTx1kz9UlUoMRggExEZYEnZeZqWU/546l2r2G/dBv9QC4KA0sumQsqdhLKMipnPUjkP0+hyfHXbdgn5tzOnTsE14P8AIOKF06RJk5LqPRYEAaVXPQbpkvuATHlCE3NA17vWoDewioWXKIqYPXu27m3Xy7RZTyM3Nxdz585l73GKYoBMRJRAyh/Pt9/Xt1axcl3vvP+RoT/UdrsdqFYbAJBhrQiQpx3timEXDU+qAE4rj0qErOcYvXPbtg16TvJU1EH2inThtGDBAgwdOjRp3mO73Q7UrCc/sMgz6N10251+y2gdoJqpMmhQFEUMG34xZjz3qr4NjyCa66UnZ0xFYWEhpkyZkjTHhaLDAJmIKM5C9Uzq3WPpVpRE6NPP2DrINpsNTRrJ+aZPvLTI72+Opp3jUqlDb2q31PUcpKeWz+zdYo0aNX3PLfrPyogXN/GqhqKFzWbztT+rRg0AwKi/3ua3jNb0A7UqFoIgoOyCW+AZqz65mNK3G9frEqCKoogXX5yvefmystK4Vqkh/TFAJiJKIOWP95hrrtC1t+mnP07ptq5IRFFEWVkpAKBj1x5+fzNnZKRNHqZJxxA5MO0AADwq/ZQ9+0S+uEm2XFeLxQIAMJvlMCNwV7WWbuvdr3/Q1N52ux1o1U1TOzat/6bS+cuiKMJ+23Q8dVxb2hRQcXGVkUbnflXDAJmIKM6UFS7eL/zG92+9B9IpQy09A7tAoijigvwtKPHIt9N3bPvW7+93TZ2ZknmYHpXn9EyxUO1BjuEuwu23344vvvgiKd5jb26w2+0GUFHXOXBwY2DQGw2bzYZmzZtrW9jjqXQvriAIcDaNfuZCk8mEW265JSmOC0WPATIRUQJ1Pr+id9BkMiE7O1u3dStzaF9+4RnDciEFQYDUoJXv8bYt/tUZ2uToPy1yPBg9SM+sU7T96quv6loaMNaBld5ppWfOnIkzZ04DqOhJ1bM8HgBkWrM0LWcymyvdu26323094VpZLBZUq1YNY8aMiXm7lFgMkImIdLB96yYcPnRY07IeRW5wzx7dff92Z7fWdVCPMkB+9snHDCuVFRh8dOnZW/dtJILqRCE6Bnpqq/KodVvHyY7vtvoC3FjOFUEQfDNEem9feE91vS4GvNQGUKo5v/8Fla4tbrPZcNVVV0X1mnsenMEJQhREUcSpU/FL+dIDA2QiohiJogiHowwAcO+4/8OBgwc0vU75064MHKQR9+o6qEcZbBk5YCgwCOjQpXuIJVOLaoqFnjnIKkGjwZ3WYW3btKFSU6Db7XbfVNXet8nbg7zj280xt0utVzvSlNxePfr21yVIbdq0aVTLT7zn7wyOy3nvLJz882SimxIVzqRHRBQD75d+2bg3gawacDjLNEc3ysDVL0bS4Xaw33YUvWymrBqA26lrCkcoiQzyjGYy6TfDnXqAnLh3r1vvfn5ToMdyHo4dOxYAUFCjJs64Kvbm77fdDIyvqG4iSZKmSVc2bViPUXmX+NrkzbXW2oNMiee9s5Bq3wwMkImIYlDxpS+zmM1wa+xcVAZByiCpXoNsfKzjbVllL5t05xK4d2/BlClT0K1bN0N7t9IlePGodFPu3fUrcqdc6wvYKnMbXS2tNZrZ2vTWuXtP3xTo0Qb/oihiyOjb4DynN7I2LoXlnssBVJyDTpfTb3lJ0pausmzJOygrk+/SlJWVoaCgoDxA1tw0SjDvnYWzBg4UNgJTLIiIYuD90veaMv1xNG+mbWS9MgZSDl6qW7+B5qBEy2CqoEC1aXuUlZUZXpc1TeJj1d7cXTt/qlQaglKypVgAFVOgRxv0FxQUwDlyNtBvJMrKyuB0Ovz+npmR6fe4svuZLhdhVYHNZkNhYSFq16md6KZEhQEyEVGMxo4di0yr/MP/l+tvRJOmTTS9zi2p9yBrpawWEG4wlVoQYbFYDK/Lmi7Bi9putGvf0ZdnW9l0GL3KvGll5IxupcgM+/dnX3vb77HWnvKRo2+E1WqFyWSC1Wr1VYVQ692n5GWz2VBLMTtkKmCATEQUJW+A+tprr8HpdEZ+QQD/FIuK508cP6YpiFFWCwjXixkUQ5hMeOmllwwfPJQusYtaDNe6XQ4KCws1T3QRjmoPcgzvndbSbEbeOfjLtdf7/m21WpGZafX7e+ce58e03t79+kMQBDzxxBMQBMH3fqfLOUbJiznIRERRUitnFQ1JMUhPGSSVlBxHbu5fIwZe3vSOSIOpAntyq9eoiQkTRkff4CglMo/WaCaT3BsW7vhoHcSnWuYthvduyJ2z4D5ZjKwIQbvdbgeWHY16/Vr06nU+8EkhAODN9z7C7WudgMsVcvlo9lLt/U6XuxSUvNiDTEQUJbVyVtFQ/rRv3bpF8cikKa/Vm9MXqRczMIjwTv9rtHTp3YtlJj1RFGG/aASmPb8AQ4cODdurqzbVtJrXXnwu7HqcQ2+HJ296xHPHyDsHyrQhLVNjVza+TYVz7D+ffY3HnnzK0NQWMg4DZCKiKCkD1Bo1akb9eu+PuyiKuPH//q/iDybtZd60DKZKVBCRLj3IanmukeogFxQUwDH0dmDMSyiTLCgoKAi5rNYc5BfnzNI0cUcsOdF6Hatoe3QrW84u2XuQN21Yh+tXHcc/fqhu2AQ9ZCwGyEREMfAGqLH0ynqDA0EQ4CyfaAQArNWq6zr7VqIGMiV36KKdWhCnaUxly27y/zOsOHToUMjF1HKQPSrb9GismJHImduiPdcq34Oc3GfZhrVfy/9o2NqwCXrIWAyQiYjibEtREYDyVI3MiqEgterU0TXASVQPstHbXbt2LaY9McfwXjm13YgUH48ZM6aiwLHkwSeffBKynVoH6WmtmBHLuaNXnBnvcy3ZUyz62gb5/h1Nz74oili+YoVBraJoMEAmIoqzDeu+ASAHNEuXLvU9nxEw8r+yEtXLZmSKhSiKsN/3PGYf64Sh195saJCsthtaOpAt3pq/kgculytk76HWFIu7H5iR0N5hLaI919at01Z5I5Qk70BGz779AAAms1nzsfNWx/n3v/8NADhx7BgA4LHVP6PVY58Z11hSxSoWRERx1qf/BarPa+0V01olIVEBspG9e4IgwNm8CwDAWbOhX+kvPZx1un3/Vt2NMDkW3gDHPe6N8kVNYXsP1aZaVkvruG3y39C5aXJPsuCOcK4F7uplIy6u1GyE8T63w6XKhGM2mTTvm7c6jlQ+F/2x4iMAgH98+hMA4OipMjSslRVTOyh67EEmIoqzbr3kmrDLC7/GlR8d9z2vnLo6FFEUMXT0bZh2tCuG5I3C+El3heyF2/7Dj/o0WEOblIwMXux2u6/n1ZxRuYk61NR48GPfv6PtQfZNP14eDfbuPzBs8BfviULU6LW5LVu/i2r5ys5GGM8AWRRFLF++PKbXeiRJcy+5tzqOqTxFp0F2I7+/nyxzq72MDMIAmYgoRqIowqEYZKeV96f9o683+z2vZdIRQRDg6DxcXn7My3ij+nDVUfKiKGL69OlRty1a3l5TJSNDF5vNhkEDBwIAJv4t+imRoxFtEOabftwk/7Tecue9YdsXyyyK4SSqUoIoipjw4KO+x1uL1gctE1j9w2q1wmw2w2Qy4fvjHsyePRs/79ypeZvxzEEWBAEej1rRv9C2btwAAJA8Hs1VLGw2G+bOnYuuXbsCAOo2aBB9Y0k3DJCJiGIgiiKGXXI5yiS5isX2rZs0v9b7W9uzZw+/5325q2HY7XaYzYqvbpNZtRdOEAQ4w0zUoBdfr6mC0b17DbPlwKFVuxxDtxMtb/k/by551169wy6vdw9yLDnZavniWmfm8xIEAc7h9/geb/RWcFAIvBZ4+tnnYLFY4Dp3IP7l7o7p7xRi1qxZUbU9XoI+cxpsFCveA6295KIo4u6nXsX3J+XvAW8OMiUGA2QiohgIgoDSEX/3Pd66QXtg4s0z7dKli9/zlozIw0JsNhtGjBjh95xanmt2dnZcbtf7ek0VjN6upTyyNHo7sfRS2mw2mDSW/lOtYlGJ/ndHw3MrXU7Me0dg5syZmns+a9fP9ntcT0PPZ3HxMblXtl5TAIBUtylcYS7olEF7vHvKbTYbrrrqqqheo6xiYTKZkJ2dHWZpmSAIcFz9GKTOwwBU5CBTYjBAJiKKgd1uB1p09j3u2U/7rf5QN2u1BmSNGvnnJqrluRYXF1eUGytXVnpW9+DC22uqZHQPsjewdBt8nz3WYFVrs9QD5GCRZtLzsmRkRj9RSMBj5TTqWns+fz1y0u9xiUrPZ+CuDhp8oXxhlVXTt0BGiAtEZdBut9thz7suYpu8/jh4oFLVMryaNm0a1fLeKhYwW+Ca/F/c87f7I7Yh8NgF5iBTfDFA1lG0t6WIKHXZbDZkZlT0FHbpGf52up8QAVSsgeWAAQOCnrPb7TBb/AMOp8NhyKxegcG54T3I5dGW0R3kse6H1sA9lpn0RFHE4UOHVdd3w213VjonWzmNutb6vf369fN73HfgoKBlAnOQ+/YfgFn//AToczUAoEWr1hg7Zozq+pVBu9PphOPyhzTuDfDJ+/+JqjfcKKX1zgk7qyIQ/DmqKjnIu3/5KdFNUMUAWSeiKMJ+82TMWLAk4R/EVMULDEo1GZaKr9CocpBDRF6xBmRr1wZ/Zmw2G8aPvzXo+XjM6hVqN/T6jHs7xo3uQa5spP/kY49g0qRJIfdX6xg970x6BQUFuPD++Tjgrq66XLNWrWNsaQXlNOpay6/16tnT73HPPv0jvkYCcLRaY9/j/Xt/x5tvvaW6rDJoz8zMBKw1Iq7fy+1xV6pahm6adcSiRYv4+6Zi5w87kvL3nwGyTgRBgOPKh+EZOSvxH0SdxePEjSXvjSjhFCPb7/nrKOzdu1fTy7Zt2az6vNYe5CNH/HMTc2+8XfUzMyygugQi1OXVi9p+6PkZ9/UgGx0fV/L1nzYcgQXVRmDo0KGq+6s+k17wVr29uQDg6jAk5PZiuQOh9hLvNOp6VghRuxg4uH+/X0PcIXKQlUG7IAho2qSx6nJqLGZLVL3hakRRxKZN2i+AVQ0eC6dbitiLXBXVrFUb9pvvxoyX306q338GyDpRfvC0JuSngqKiIlw49VVMO9rV0BM3lrw3okTzeCrqkrqcDhw9clTT6ybfOkb1s6QlvhFFEZ9++qnfc46m56l+ZgIDJmtWVlxmZFPr2NXzM+7LQTY4Qtalg9psCbm/Wsu8eWfSGzNmTNhe53VfCkkTXAQKbLbH48Gm3xSTbwwYBTQJXZVEGbTXqF5N83Yvvfq6qHrDA3kv7NavDy5dF7XqdWKecCSdnT51Eo4BN8HT59qk+v1ngKwT5QfP4/FgypQpSftFFQ1RFOHqKw+IKC0tNezqN5a8N6JEs2qoOqHG6XKq/ghoGRSmVpPVbLaofmYCAzyrNSsu0xWr9YLq+RmvqGKRAgEy1KuMACFykFVef9vkv8Fms8Fms6Fly5Yht/ONUBh1R0ZlqmZEI3DWwH9u3o9tjrr+C3UeqvpaURQxadIkX7qKRWtuCoDGzZpXqjfcN7udHuda14vwySefpEVsoKf2nTrDZDbF7Q6XVgyQDeDxeJLqKqgylF8qkiThzTffNOTDHUveG5EevClE+fn5UacSZVkj1y1Wk5mZpSmgVaNWk/WqG25W/cwE9iC73W5D0qUC17fr1+AJH/T8jHsDS3diZtKOOu3sxRdfVN1f1ammI+xTtWrq+ccAIMGUMr89m/edCH7SFBySbNqwHoNvm44Fi/+FBQsWYMiQITjyh/ogRSP4ZrfTEJRHDKIvuAkulysljk88tcnpiPbt26PNue2T6vc/tu4PCiudekH79OkD/K8i98r74TbiBPb2kBDFi/f2aVlZGTweD8xmM7KiSEOwqHUBavDcwjdhs9kg/OKfkqGll0qug3wSH/9eMYNfsxatVJcNnPzr7JnTmPn8TFitVl1/iOQf/K6+x7/+9COA4Nvlen3Gve/7WuFziA1KDPveUDsau3/9GQ89MQ3Omg1RTWOwf8+0R9CtWzdN7VTb5tai9VixbWPE3xRTnH97RFGEIAhoc35w1YpAgZ8Ul8rVoLV6DQROtv7Zl2vhHnEvsP8HYOlUOJ1OlBw/BmTXir3hUfBe2N334U9YV1r59Vks6nd7qrqaNWuiSf26SRUDsAfZAOnaC2pk4C98vRZ3P/5C3G49JeOIWYo/7+1Tb8pCtHd/lPGx2WKBSeNsW5179FJ9PtY6yEXiV6rnstqgLSPy/AO/E9p2OE91Ob0+d38clnsQv1rzmaFjI9Tev19//EGezOHiyZrfR0dmLe3vt8o2x1+X5xvcWFp61u9vysCz3+ChUf/2xJo5oBx0ecstt0RcPrADVq0CiSXTGvTcfm9Ju1qKkmcq0z5/f/gMWj32GYpPRz/1eyQ2mw29e0dRxhEVU00H0tITTcmBAbIB9B79myzuuH+6IYG/KIrIfelLvFSSg2GXXGF40MqKGeTlvX3qTVkwm81RXQQqcyHH3/U3tG+vbepjT4hIONaMgfVfCarnslqAF487XGq7p+fn7sD+fQDk4M7IlAK141GjVkXPZabG99FSq77m91ttmw5nxeDGM2cCAmRFvNWz38C4/fYE1iaOltoAS5W4Fyvffw8AYDGbgWseAe5bCUjBC85bfxD7TpTi9fV7om6LXpS7pJxqWokpFqmDATJpNv7u+wz58hUEAZ66zQAADpgN//JgxQzy8t4+nTVrFhYuXIhZs2ZpvggURRGnTv7pe9yznw01a9bUuOXQoXAsPaxSiJ7vwEC1eo2aut/hEkURQ27/h99zb7z0vN9jp9vj97mr7IDfc8oHqpksGbBYLNizZ48hF7pqvatnTp3y/XvZyk9876NyIFkgZ94Mze+32pmRYcmAqXymuRo1QucgxzKoMNaLMuXFZSy9oi6VBHLVoLn8KbezDGjdU36gspw3ZSMjSXpolVNNK2VkZDDFIkUwQKaEs9vtvvuEGRnG58+xYgYpectHTZgwAZ/WHYJnf4o8NMPbG6qcUvfecf+H06dPa9pmuEAmlh5WU4ie719+/dXvscVi0f0O15ovBDgvutvvObfbv4fv/g9/gN1uh8ViAe5bCeneFZUa8Ostj9a2Qyc47lqGBeYLdbkbpCUH/NzzOvn+3ae/PIOhKIqw2+1YsGABFixYUMk2qD4bsn3Kp2Ipe7d+XWzvmc1mw913y8fd7XZHWDo4tUA9GFZpvzdtSdlrrNKD7I23zTGOC9Cbb6rpAJbbC0J+/tLxbmYqpzMyQKaEs9lsaJjdEAAw+5U3DL9FyIoZFMr/fi3Gf7dFrlPq7Q1V/lC7XA6cOnkqzKsqhAtjYrmz0X+wPehcFkURz32wTvM6YnXhkOCJKyyZwdU9bDYbxo0b53sc661mURTxn38vBaCollGtli53gwIvXNTitTbndgh6ThCEmNIM1KiVXXO53ZAkCW63OyjFQrl0LPnEl424WPX5SIGNKIp4/vnn5fx9DRvWkoOseuFoKp/OXZF/UbtOneDXlr84mhJwetPy9p+xqN8BEEURg57/TN8GJZgoirjw7/N98yg4Hfp8RuKFATIlhczyclmdu/eMy/aMmCkq0YqKilL2Sj3V2O12ZGRk+AXIZrMFtWprG1kfLp6IdGdj7dq1+HCzf89wH9vgoHP5v4XfwNOym6b2VIZtwICg58ZMukd12TFjxvj+Hevdm4KCAric3loHFcGQHneDAnswtc5MZ7fb5SmQw9D8uVTZpDWz4o5XuBSLWKbedjgC60bIbR32l2sx4/HZIXvm1epxR0OtioWq8h7kGjVrwFReBq7tue1Dru/zD/6bkt+BgiDAc4764N1UJQgCXANuACCfZ2UO/QdQGokBMiWVpW/mp+SXW6KJoohRo0Zx4GEcud3ugFFF2nuuwgVe4e5siKKIIdNfR7EnK+I2OvVSv8UbDy1atw16zlsSzCuWuzeiKOKNN94AymcwVFYNGTt2bGyNVQgMMH/8YUfY5V98bg5EUYTNZsP8+fNhsVhC5uNq/VyqnRmL/rMSt912W8R9jGWq6QyVyW4EQUDp2IXwjHstZM+87yJRo8B3RWs6iDlDvvBo3LiJbyUWlcil5E95PMCH/3kHuYFTrKeAdEz1U+6TJTMLWdbI31vJhAEyJQXvrZfFC1+MW4AX79woI7fnvcXLgYfxMWfOHLh6XAE0PMf3nMfj0p5iESY2CHdnQxAEuGo30bSN7t27Bz1nxEQh4rrgNI69u3cFPeetYOElCNFPiywIAlwuF9BIDsAlRTC64GjzSn93iOv8pxP+x8Mzwi7/9KxHfdssLi6W2xTi4Gr9XIY6N9544w0sXLgQe/ftC/naWHKQb7o5OOj2BTZZNUL2zHtTZrQO0DMFhMihKrkE+r+/3gqgvKRi+f6pTdF9/IQcIEtup2qveDJRO0fT6W6ml3KfXv7Xf313ilMFA2TSbNH85w0LJr23XiR3fGYhjHepN6O3573Fy4GHsfFevGhd9oMPPgCGjPN73mzOgEVjj1q4G9NXvbEBW9RmGYP6LHoAcHD/Xk2B79kzp3U9B0VRxMUXB+ew/vO1V4Ke81aw8Jox+/mo2+Hb/3Pl3nFJGXSd07NS3x2iKOKyK67we87ZIy/sa5QXpMrBv2q0fi7VwsYV/34XDg8gNWgV9uoqlhzk/7vppqDnlIFNuJ7+MWPGoFq1ajCH2OdwtKZYXD3qRgDArp9/9F18nFFUj/GylPc0myQJVmtwPeV40DoddVW6y2fxznoZezZOwjBA1kkiT/Z49YS+tKrIsA+299aL2RJdHdpYxbvUW0FBAUpLSw3bns1mw9KlSznwMAbKixctBEFQ/SEcMNgOt8ulaR3hfkhXbD+M3AXqnzGbzYYLL7ww6Pnl776tOfDV8xz0DVYM3IZKbqrZbPYL7j3dL426HTabDS+//LLvsSXDPxAyW6vj1z37YvqOEgQBZU7/42eqFr5sn/KCVDn4V43WFBC1QXowAbhiKjD2JcASOviLpQe5/4Dw3xXhvku8+zx58uSI2wlKsdAYIHv3SXJXHJtTf5YELbdn3355OyZg7ty5mtat1ezCnfjX5v1RvWZLiIlCAGNrdycTURR91UUm33IDB+lVRd4fWOXjeG87Hj2h0oXjDftge2+9jJk4OS4BXjxLvXnzJr1BkdlsDtqeHhc5ffr0wd4Ol6Nd1/Mr09wqR3mxpIXdbkdWVnAunfjlGs09yJFCA2eY7pbs7Oyg5zwed1Dg+91336m+Xs9z3vs5Ct5G8K1UZ95MvwDZlJEJq9WK7OxsjLrjftw+aZKm83/ChAm+f19y9XX+25j0LyyqcUlM34XZ2dmQul/m91znrsFpKkpTZ/zD7/vKO/hXTf6S5drapXJyXHndDcA5PeQHYVIatKYtRNhcVGw2GyYqjkko27Zu8nusNZj3BtImRUvr1qsXtJz3boLkcuK9997TtG6tpn38I46fjS64Wy9+E/Jv5sbtVH8D0s2qNV/6/u1yuzlIryoK7EWJ55VhXHtCPS7Dg8luvfvFlJsYrXiWevPlTZYLHPktiiIGP/5vTDvaFcMqcZHzc/FZvLr2d1z++vrIC5NPpFvjgbznTiC3y4mzZ89oWocUy4wOkM+VH3/8Meh5s9kSFPhu2rQpaLmsatV0PedtNhtWr14d9PyocRODF27d06/nvHufAZg7dy7ufOQZ/Lv6hVj4/RkMHTo04vmv/Ht242aqy8TyXVhcXAxccKPfczVr1Q77msl/e8BvopBwF7mecfma2qV2ZvTs079iGuYwgeWRI38kbSWbSWNu8HusNlGImh9/+AEA0KlrN1++c7169YOWM1nki1PJ7cbnn39emabGTLlHvfpfEHI55w3PBX3+0rFHueeAivcgw1qNg/SqosBelHjmf8azJzQzw6LLSPFwHrpjXNzyguNV6i0wb1SSJL8vQ0EQ4D7PDgBwOJwxf1GedcqB9xmHtp5QqjB27Fj85S9/0bx8qHNGay3cH7Zv07wtL1EUMWzEZdjuqBv0t6tuuDko8FXrZSsrLfWlA+hFrcxbs1bnqCwJv+/JDt17obi4GK7q5cFOw9YRA8j8/HwMUdRd/uPQwZDbifa7UG15rdcxa9euxeBH38WM+W+GraCgpV2h4t+KeDJ0o77+4vOovz9jyVsGgAfmvomLR4xAfn6+puWdLv/PhtYe5CcfexgAUK9uPXgTNU6dKAla7pzWrcv/Jfl1Qvxx8EBCLho69+wd1fLpOG5kxqaKY/7UwgIO0quKAnuU4p3/OWLECPTu3Rtz5841dNvOslK89tprhgavTlf6TQHtzZvMzMyE2WxGVlaW35eh8t8Zmak3wC6e1UD03pY3RSk/Px/Lv9rk93wsTpwIHjyk5h9/uzumCg5lg8er/q1Zi1Z+F3uiKOL5554LuR6jhYp9lN+TO777FtnZ2X6lwsJNwyuKIu68806/i5Ctm9TzPJ97/oWovwvVlvdESEDwlnn7+Iuv4e4yHJ6r/hG2goKWnnvVHGSlcCkW5ZOJqH1/RjMQ1a89Kgdz6rw38czehvjsVENMnDgR//73vyOuR8tEIWq8szKeOnkCUnnd8e+KgiunZGbJ9aEzMzL87gZ98v5/ElL+0hXlqDS182LXzp+S8m6AVjsOV1T16dC1Z+IaEiMGyDpJxKAoURRxwXOfYfmatdiwYQMmT55s7IfJ7TI8eM3MSM8poCdMmID//e9/mDVrVtCPpM1m8xXAf+Vf/02pAXaiKGLgsqOYti3T8B+gr9euxbDci3T9sfOmKHk8HmBsxeCvgoKC2FaosVfM5Yr+ToHdboepevAMYmrCzewWj89VqNina6++vn9v3/YtpkyZgry8ikoRahU6vNQmpjh08IDqsvdOuSfi+bGv5Czmfvlb2GUixXDeMm916zcof4E7bAWFwHSMbduC7yREOoWyGzYK+TezRb2STbQDUZXU3oNPvim/mKzXHABU02yC1hOwIq1VLLypJX8eL65Ylzt4MOyZs/IMgw8/86LfQEm3Sn5+PETav8DzU+18/eXHHSlZ01lNLPnxicYAOYUt+VyE1LoXcOnfAMRhZKzkMTx4nf3KG2lbiSFsSkd570r33omb3CEa3h94XyDZrKPh59/g94pROmmJrj923hSlwMDszTffVP3BCteDbbZYwvbuKZna9ILr3NDnt1q9YpvNhv79tZ0fdrtdtfRWpNne9LL26y9Vnx+/dGvFA5MFDocDu3ZV1EwON/20d3Ck/7FSf7/LysoiXuQMeukb3LtiOx74x6zQecMRolXvuXj0WAkAoFbNmqr56UrKYPXuu+8O+nuR+FXY11vD5HH2G2RX/f4MNxD12WeeCrs9tR7k/v38z0O1Un9B6wm4uNEaIN/7oBzUZynOXbXA5eChPwAAHbp08xsoaVHJzzeK8q2KtH/Dhl/sO+8CB/orV5jsNZ21iqXCSqIxQE5hPc7vI/+jfHCC0V8AjRo11DSbU2V07t4z7aaATjfePNAZM2bg9ddf9z0fr15/s9kMk8mkWs0hWt70qFmzZvk9rxaoiaKIodfdgunvfK76Y9aqdTvN23UP+iseXn8y5I9GqHrFaoOTAPmHOTB4VwsdnU6n7j39ahOFrPe0VF32P99V5AybyoOWgQMHlj9hCnsOqR6rMD3OoS5yvI6cLAUAPPvM0yHfE7W75MveXuT7tzfw6tNfzsOuW6dO2O8u72yC3mBVrZd//VcCAODMmdMh1xOKR1KfaCbcQNQnHn0k4joDec//7MZNsHDhQlx//fVBy0SqCuPUOEiv9bk5AICdOyp628/rGjyFunfSmJ+3b8OjT1YE/ZdefZ3hv1tqIu2fo0Fb33dMqHKJgPpMh6kolmnQE40BcgrzzpRVL7shbr/9dnzxxReGBpZmkwmLFy82PA+Zkpcoirhj2mNwnjsQHo/HrzrH3XffHZcLG4vFAo/HgylTpuhyDtpsNtWgbMOGDX7rFwQBZaOegTRiCsrKgssV/b7rl6hHPG39NvRgvWh6yvfu24sLH3gZMx59HLm5uSgoKFAPUMp7pPTq6Q81UYgWDdp1xdixY9GmdRsAQOt2ORHvHAWVUetxWchlw/VGA4C7/Da95HajrKxMddnTp4ODVFGo6CG+cewtGDt2rK+3MMMS/g7CsNyLkJ2d7QtW1Xr0vafQmVMhZmUMs4kNa7/C1KlTg54PV6M5UiAbrhf9/AEX+JXd819v+JrgLpVa2arrKV9MmVbhUisXZpYDycem3otHirv4/emN1RuQ/9rrcf3dirh/iov8UOUSAaBHjx56Ny0htN4xSCYMkA0Q7ymMm7VohVdffdXw4MR59nRcJ9eg5CMIAtw3PA9c9regvz377LOaR7RHS/lZcrvd8Hj0m3FR7famu3kXLF++3K/smDKI9vS+OnhFMdxC/O67b0P+LZrbwmv2nIWr3yh4+l7n64lSTacwmXTrfQfC93xFUmzNxsKvf8H0GdMBAK3atNPtO0zLe+ebIvnSv8HjkVBSUhK0zO+7d4fdzr/ffQevvfYabhl/GwAgwxw+QHY064zi4mJfsDp//vzgdpX3iteoVSvsulR1uABz5sxR/RyGqtEcLu8bCF8nOdwgMovFv+czMyAA1NqD7J10xqxoSaNGjYOWq1dfvrvi7HG53/Mb9p6A46pH4OmVp+k7I/D3O5rfceUAy0hl7DwX3OR3kR+qh3vjxo2+f78y95mEd0xpjW8C//5jDJV7Eo0BsgHiOYVxPNWqWVP3knLeD1siZtiJ94VMWOXfpf3mfY2BL34d0yp2lNcL3X88RM+TDux2O2CVR4vjvpW+H3NAru981113RZ27G4koiv7BqccDs1m/GRdVg7zr5Nv4yh9Uv+BtcPCPmZyDHN22u3dX7x2qXqNmUC6pKIr49ddfVZc3lw9kMlWvDavVijFjxuD6UaNUl3W73bjzzjt1uZgJ1/OlhdSyKxyZ8mx1v/y4Q7fP4vjxt0a8pe7LrT23H1CjLl544YXgZSJsx+lNlSgP4iIFyOaMTF+ZvYceegjdugWnCvQbJJexq1FDfRY/LadYNDPJKQPkHd9tDfp74OAqURSxaJGcZuIdRLZla/DrAtM57p/5mN9jrT2Kv/0mD6S0Dbb7LmqyGwUPVPTOghg4kLXULOdsmxq1ifidETjxVn5+Puy3BHcGaBFx/5qd58uVH5Z7EfJXF6kupswBf/7JxxIaV2iZmOzLX4vx+rrfgy5EtqucW8mOAbIB0rWXtVatmrpOrqH8sB0tPqpTK6PfdqIvZBYuzPf7IRZ/Px71OkRRxLTy3qE/ncBXX4eexakyAo/5Q0/4lxILlbubm5uLaUe7YuCyozGVN1PL1dSrrKHdboelfXAtXyC6vOrxd/0NrULU/w0lVA+yxWIJKtuWm5uLn39Vr7qQVR6kNmzWEnfffTcefPBBvK02SE2SIEkSXC5XyIuZaISaKESzzsOA4XcBAA5lNcWQG+/U5bO46FAD5L+xOOxnW9nDaYZHNdXApDZ5jGIgpqW8pFhGfbmaQ0aE3ti7ps6EzWYLX8Ui7Bq0+eGHH1QvgNQG3Cmf26ZSNk8Z53nPw88/L08z6TgYpW1t2LAh9LTKXk+/73/hf7ZM252HV1+aBwBo2KiR7723qAyGPVsqp100qF/P73l3eTpGu87dI/5uBU689d5778HZPnhqdy2cGlJIPB4PDh06hLLzhsFz1cOalk9kXCEIAsrKyuAOk5Y05JW1uO0/3+HoMf/fMZZ5IwCI28Qd62MIpKJVVFRxVZthNuk6uYbfyOryL2GXR8K2g9pqyeq17Xh+4ajdvrtTZSR7tAJn6/v3x4W4ZclWmP72AZ588knde3W9njxybsWDS+6FJElBt+8De2g/X7Mmqm1kZ2er3gYuLi5WWTp6NpsNF00K/nG66qqrosrrv3HCXWjYMLrUhX8ufkvTct4fJt90wwE8Lvn9PXL0KObMmYMvv1SvIqHkcrliL2enoDZRSKycfUZizpw5qn+L5nx159jgGXij5s/2vdMfU50+vFmLVsEL51Ts7+gb5QlaHJfIvYyZEXKQ2+R0jFjFYuM3chWLWAbpKXl7eZXUsoCUg8Bq160X/BpFyF7xWa54Tuo4CPVVJqU5Weafg+ydDMnL6dI2oZF3cJdZERSrdtSXf0dUC5iM4vSJYwCAlm3bR/wsB068de2110ZMQVFSvr8/7Nih+XXmbPVBrTjPPzjX885ZLLKzs32lFj0eT9B3/UdfVHTMPP/sM35/a9uhk/EN1BkDZAPEYwrjbQf/xF3vf2/Iur1EUcR1k2f4HpeePqVrWoJaia1nhd/Q/dn/YcchY4PkWGcgrGyqQGCvtVptV++y0bDb7X4/dE269MNbG/cCAKbPWwS73e63TkN60DsPhdlsDgpcA2/DD75wSOArQxJFEVOmTPHr5VKbbCXUa7Ueq0Yqt2w//vhjFBQUaH5vtm8Nnto5ErVjryZwNsZAzjK5IoN3oJIWkiRFrPSQCMuXLw/q/RRFEYPmCZj+z9WaP6sma/WQn21RFP0C0PVfCxgxYkTQclnVqgWvuEtFvvr1N9zkl9dbevpkxHYFXpwH8p7rIQfpabRly5agY6vWO33R8Ir9Xvj8U0GvUfYgez/LytQqSBKeDJiAZGuRynT3Gf6pOJJZ29Tulgw54LWYTb4dOH70j+AFTfL6gu7iuOW7T7t2/RrxXFcOZiwsLMSECRMwxK79+2rduor1P75ZZSChik8++QRde/TStOzoMeMSVgJVmVoDQPW7/n/fKN7fax7x+xvLvFHc7C056/fYiHzaT9Z8Cce1T/geHz9yWNegymazYe7cuTC16wPUkKfP3fC7/IH74bBxebTebUd7IbN27VoMXHYU04WDMe2/Wq+1t7ar2rLRsNlsfj9SH69R1FK9/kk4HA6/3sJYe9C17HNgr0LgTJP9B0R+r5V1ln0TeZS76KKLIqZXRHsB8MeRI0HPORwOLFiwQPOxnjz2etWqB3qw2Wy47777Qv69evXyvHBLhDrH5YP0vCJVekiU9957z++xIAjwtOgK6ZL74LhrmaZ1nNetZ8jPtiAIftHi153GYXn25UHLRRpH1qf/AL9z46dtW8OeKy6P5Lsj4v0vSPnxCT1IT1uiu8fjCTq2aikWjZo2qWifK/i7QFnFwvtZDizrFpgCtXFt8DiKGnXq+T3WOEYPf51wBwA5KPbOpPe/Tz8MXrD8vcwIfEvLq1/s2bNH02c58C5pNANav/rf/zQv6+VwOPCt1Cz0AjXq+f7ZvGXLhATH+fn5GDx4MDZs3QaMfhqACZmZmUEXnwOUd5PanO/3N5Z5IwDxGaRX6qwIGM6cOW3INnsPuMDvsQmS7mkJxcXFcOfNAMp7E8rKa/r89sM2wwfQRZsuskaQv/ykzsNi2n+1XutQOZyVvYUm/ryv4kFGcAAeaw96pFvykiSpll+L5kvdOyhv+vTpeO2fSyDZ/s/v76t3n8Ydd98TdpCZllw55fY2bFTp/b32MeDmeTh79qymknJulxP79u0Lu4xWTqcDkyZNwqRJkyCKIkRRVK144FWjutzTacoIHyBXr1ETEydORGZmJkwmEywWS6XONVEU8dTTT8f8+lCuvfZav8extLFD564hz7vs7OzgOLNuk6DltPymLy+suK0sucPPkPj3D3bgjjvugMvlgtlsxg033BC0TOtz24fdXqTwuHr16kG1wr0XnGtValaP/r+bfP/OyAj+LpACcpAFQUDnzp0VDTIFVUyp16BB0HacATdLtMZLzcp7hI8e3F/xWpdKCbny2UiP/3HI//nyHmSYM1BaWqpLWlEog4do723WKrNBRfA84ILY8qErQxTlKd7dbjcw+K9A807AeYNxyy23BH2+zj//fPWVQL2meLJjgGyAeOS2liryt04cP6Y5GIhG7969/R43bdZM9/zqwHV4yk/JGXeOS4oBdEpDFF9+sex/YK81AMwOuDWpXDYaykF6AIBa/j9QWVlZGDNmTMi2aNmeKIp4fcXnYZeRdKiz6+01liQJ7kv+Dk+/6+TBXF5XTIX7rn/jjn88G/LciJQr55Wfn49Bgwah+HhJ8B9b9wQatQUg10QeOnRoxLafOX0m4jJKodImys6exYIFC7BgwQIMHToUBQUFKAtTTs1SnpTZofv5uP3221UnhADkwX9jxoyB2WyW31+3W3WgmBbeXvp//OMfMb1eTaY1Cw888EBQbd1Yes2OHT0SdJEtfL0WY+6YgrvuukvTaLhIM+kVrV+HHn37+x6bJU/E7wW32w1JkuDxeFBLpZd43++7AQB7fvslcgNVzJ07169WeH5+vq8DZcSIS4KW79u/otdv4n0PQhAEv/fMI0kQRRGTJk2CPW8UZjz7Mh57rKIiRet2OXjzzTf91jnroeDKD5JJW0pFIG8VjabNW/ieM6slIZd3sjRrFtAb6yoPkFt0hnROD0PTirTcHfNjrQGpdsOwizz34kuVaFHl+aUBtpAvjCxZNfx+T7RgigUBiM8gve0/7vT9u+RYMTyX3Q/ctzJsMFBZDerX1z2/OtQ6nE6HL+B/5JFHkiZIBuT6qbHuv7fX+q7/ncDAZUcxc+bMmCdaUAocpKe8LQeYVAebRduDLggCXDc8H3YZ3QeRZJWXurpkStCfPA1bhwzEi4uLfcGnWq4cUD7pyR13yF/+lsi5u0ZM+dpPww+qw+HAoUOHYM4IXU7NO4DJ5QHOOecc/OUvfwm57MBlR+E4/xqg/QVw12kaczULb5qOJ8JEE9FwOsrw7LPPBk12EUv7vvnic7+LbFEUMfSfv+Dt6rmqVVHUROrlXPv1l+jYuaJUW+9+AzR/njweD+rWrRv0vLfur1o6BICIXchbtmzx1QovKyvDe++9V9FpE2G/X/lsM2a8/LZfXfDFbyzCkCFDsHDhQjjGvAzPX1+FW/FdU7d+A/Tq2dNvPS6VHl5XjPGRNxWjabNmMJX3El98xVUhl28eGCArr4S6XBQxrSiu5T9vfQ24Mbi8YCg3XX153H8L7XZ7xR2Chq0BAGNun+x3nnvfs3+9+27I9aTiRCHpMYdhkiksLPTllxqVL/T9jz8DaF7xRIfydIgMK7Zs2WLINi3lVSziM1uaGS7IPyKff/45vvrqq4QNTgAUM4bd/i4kSfLdpou1PZuPyD9Ubrcbkg6Bl91uh3nBu/DdxVLUAjWbzUHtFEXRtw9jxozRtB92ux1YFr4cn8laDXPnvhB2fc88/RSG5w4LuUyvXr1gsVgizvBldpWFDMSzs7NhsVggSRLMZrPqRaMgCBXb0DBgyGq1IuKwmyjrIK9b+w1wfXDuq5IkSfjwww/hVkmVCdzsr/sOYsbSZ2AuPQlktwm9Tlv5rX2PG+4Xr4UgCFGnwezZswdmsxluScd7p626wTNlOebMycO5556LCRMmVEzkMmlpVKvyeNxA+Z28goICbNq8BRg0Pap1hAxSy9VvkI2zzorzNJoqJiaTCSdOnADg34NoNpvlz3GMPW6vv/66fNFXrTY8NzwDq/tbWK1fweFwINNqRWnA8srNuHtfA/S+Bo55FRPhTH1xMTyNcoADP6hu74+DB7AwPx9Ah5jaG4l3RrqIVSzKBVYSOadtO+wp30dThOnMveldTqcTmZmZ5YF0hLz+yqhWO+IiW7dsgfe9dTodUX9W9eBu2xc4XjFNfMs2bX3pNiUlJXjhhRfgcrkg1W4E3Pq6+jpSMEBmD7IBvFPXBt6q0pO1RsWtOeWgG4ycZdgtJG8RfD2vsEOvo2KfEl37EZBv+5eWVvy0LFy4UJf0D2+Payy8x+GzL7/BwGVH4RpZMaASTXLCvm7IsIuw4H8/YcGCBRg8eLCmSSO0fClLtRpFLL/2yL8+C/neKatWWCJMvOE+e1I1PUAURdz1yn/hHH6PL41ALYfYbq+YeADt+obczuDBg9GpUyf0798/5DJeWdbQQWw0LBkZaNmyovSTy+WCZArdn+H77anbFJ4Ji+XAX6VWbBCzRVNFECVvwLpw4UK5J9aIW6cZVt9APV+JuyiZzRZYLPJ/r7/9LjYejn4dkX7TZz74d2z6rqKaUIbZHPE7wVQ+OK9atWqqOZst27SLup1KbrdbrhhxxztA/eb48Eh1jBgxArfddhs+/vgTTetQXhh4rpwhD8wKUSHl8MH9ePHFF/2ei6Y0WiTeu/tHDx3wDdJb9f6/Qy5/7I+Dfo/r1qtIN2vRum3ICWREUcT48eN96V0OhwNz5szBDz/8qLmtkS6oYlG3bkVnh8fjwfbt23XfRij5+fm4bvT/wXXZA3493ft270Jubi5mzJiBOXPmwOl0Rtx3BsgEwPhJKERRxLI9FY+bKHKz0KClYSPTLWaTrvuWn5/vl9erFHiLLiMjw5B0FWWw782z8w6MUi7zxhtvVAQCZrlnsrS0NKb3+aUFFcGo2WzG888Hpy1EugARRRHDhl+Maat+xohJM8NuTwro4RMEAc7B44BL7wWa5MDtdusyaQQAwFUaMcVHatktZK68NxjyeDx+9bFV1WyAO+64I6jdgiDAmXunr4ao91gFDs7Ztm0bpIZtgftWhm3v2rVr8cMPP0SuLXzuAJRVDx6cFAu3y+U/4O+Cm4F2fUIvH/DjlJmZGTIPOZBaebNwvMfIiGDA5y8PoWf5bXtlPnk0Lhh6EW677TY0b94crv97Xh50GaVIv+lOhwObtlZcpGWYTREHgb300iuYNWsWCgsLVWfS21NNpfZyFMxmM9B1eMUTnexY/slnWLx4Mb7XGFypvt/nq6ftSJIUlGYz8sa/am1uRN5z+/D+ih89jyt0qsjKf73l91hZfnH/nt1YuHChatlLu92OH8pnI0XHC4EGrbBy5Ups/97YcqqRzN1SUTpQkiS88847QSlIRsjPz8fEiROxf+SLQX/b/etO/+pCtbKBcQvl9y0E5iATAOMnoRAEwe8WultZcD3CLaTK+PPYUd32LT8/H5MmTQqdCyh55Ol+L5BHWPfv31/320r5+fkYlHcDpm12Y+BFl2LgwIFYsDAfCxYswJAhQzBp0iTk5+fjkUceUc2pkyQJJSUlUW1TFEVM+UfFqH+3242tKtO0RroAKSgoQOm5g4A+10DqOzLsNgO/lux2O0zegSHl5fXcbnfEY6mll9njcgZNY/zf7w7i/W2KXp1uF8Pj8ai+d1EFQ5dMUW23/7kv96Kq1fx97733gEE3IZJIqR4+l94LZNXQtmw5TT1tjdoC/a8DRtwTcpHA6YCXf/I5rrzySk1tWL58uaa7CN6LyaALoLahA/eY1W2C+fPnQxTFmFPGzrqBBTUuw253baB2cJ1rLSLl7GZarcjp3NX3OMNiwo4IE0R06tI5fO5/jG31ku8eBFwc2W/F2Ztfwb8+EYKW13qhYwqRA282mfzrIgPYt2e3pnVq4c1dbaGobxzu3og7IHj2KDoIJI/H1zt8xx13YNKkSbj66qsxZcoUeYxBzgBgwlvA5X8H/voyPOXLa/XG669pXlYrqUlwVZN33nlH9+0A/h1GgaUWldqc297/AnzCm0C9ZsDg0AP32INMAGIvoRXN+pWU9TKtWVmG5equXbMa2dnZld43b9mYsIFQh0FAq+5A/+sBa3UcUalTWxm+AVrXPibPTnbuAKCTHbh3OdDlIjidTixYsAATJ07E6tWrg9t68WTgvpV4ft78qHpeBUGAp0FFj7/UpjfeeuutoOXCVSTJz8/Ha6+95gtuAytWBJEkv15xm82GAQPkdAFvLVYtt9nDfWEqt+VyuXD77bf7Aq5rFxfhmreKghZ95plngoKy4uLiirSHC28Bmpwb9LpAJSUloXvcMysmenA6/Utw9QwYWBTSheOA69WrjVSWx61SrgoAqimqG1xyb+T1BDy+7KMSdOzQMWg51WC/VoOQdxG8d1WGDBmCwYMHY9rDj2LiPX+r+DxYMoCrZgSvUwfe3OE33ngjptdvP1qeUtH7qpjbcPJk+Ik/rr/hJpQpCvqWHPkDXx8MH1S//fbb2jbetCIw+s8/3wyzoAatewK1svH7eVfFvIpbb7vN9+/u51dUOGrX4byguxXiV0LM2wnkvfhr0bKVb5BeQ5WJfUIxhQint27digWbi7H8C7FiquwLb/H/Pr1vZdAEJ+HMfe0tzctWxqFDh3S/Mz116lQMGjQI06dPR25ubtjvx5Zt2uKyyy6Lav2p2IPMQXoGsNlsWLHqMwhffYMrhg2Oa0K9tTwHcvbs2boPEvQ4y7BlyxbMnTsXixYtQrVq1WIarBZq9jg/XS+q+PddS/Hz0gcgiqLqdryDBbKzs1FcXBx2v73L7tmzRw4WataX/zD8zoqFRkwGul0MLHkgYvtcMOORRx7BI488ErZt3jZlZ2dDuuz+igWGjIPrn+o9g2oVSURRxKQ3PoenV17FAA9vpYcwFi5ciMWLF/vKyxUXHwNQG5OnPYrSjeFTDLx69uyJ1SHiOZ9bFwGWDEiFr+KOO+4of1KlCH7bPpD2bMVdd92Fbt26+d47b16w1CsP6HN18OsCmEwmvPDCC/B4PLBarb4BspA6y3VRrdUB51nfssqLgHr16gFBQ5ZU9Lkq8jKxOhsmADOZ5TspZZEnzTl54k8EDiaavSe4fJTb7ULQ1/6Et4CXb4DbedZvAJAoirjwwgsr7p789RWgQXle9PN53kZGbFusTCYTDh06pL0HP4DZZAqfoqOF4k6dmoI3XkPGt4eAIXLwePTgPnj+8lDY1xw+fDjqZjz+4H3APe9H/Tqv6rXq4CyAOvWzcfCI/2Q2f7/nLqBent9zt99+OxYErOOcVq2A7T8BAMZOuAt/+0DuKXc6nUHf51IMKTGheAMri2Jk3h8H9wGRr53ltqg9eW5/eSKLHpfKvcb/Ki9LV6ryWWsavi610q9l0d1BikmjtnCf0wNz5szB++/Hfk4o5efnY867nwCZ1YGy0ygrK8Off/6Jq666CstDvKZp06ZRbYM9yORz8YpjePJYJ0OC48ActxPHj/n+XXr2LC7IHYFpC/+NwdeNQ//+/ZGfn48VhV/jH088jfz8/NgH2LldyF/0BiYu+gwbBs3Al33+jgVLP8CQIUN869MygC9wWmQtPM27qPamenOip8+YgYnb6mF6eYmiUAPABs9eiekrv8Ubb7wRPkez+XkV/84+B+h5ufqgJ48Hn32mPuhMFEUMmfw0pv93I3Jzc5Gfn48pU6Zo3GNZ4IC3gs/Ww3PBzXJPR1aombaCefNw58yZg2GXXoGfnXJwfWDvXixevBivvfZa2JQOURQxb968yBvylkvLnQS3241Jd01WX+7qh4H+o4JSJJYvXy7/2Ia5Vee3X5nV4XQ6/VJ+srOzAUf5TJPW6nJvf4vOQTV/s7OzfT1SmmicGjcqrjAVTC4uf+/UfrQDHFd8B4RjCVXOrnySDO8F2csL8jH8wZfhqtdSLu00clZFcBwnbrcbH374YcRaxKGcPiVffDRo1FjPZvk7bwhcqDgvmreM/B59vvpT5Ofn45p/LMDjKzZq2kw0FwlmsxmmgDIPNWrIgZvaW7lY6h30nFqN25mrfvL9e8fPFTWa69ZvAIuOg/ICHTggp2fJX7/lOxBNAB5YZaVmA+DK6XJwDAAeN9DvOrm3WMNnLaxLQ892qZub5wFDxuGDDz7QrRf53eUfAdc9AVwmXyhIkoRFixZhxYoVIV8zZsyYqAaYM0CmII88/oSmk1gURVx99dW+gDbccov+4z/NZom7oufIZbFCmvQOcO1jcI+agw1bv8fE+x/GVR8fx2PHOmPixImYNm1a0CAFTSQ3PANvAgYpvjxveRVOpxPXX389RowYgQsuuADTpk3D4MGDMWTIENX9sdlsUd+eQY26IUt1lZWVQarbDLBWh3TRXSFnSxIEAe72AyENvBFutxsdOwbfglY19iVg2ETg8vtV/6w2YM9bjcF54XhIF94Ch8OB1xctwtnS4B7LcHVkAy8K/KYkrR65RJBPZjVIMGH58uUoHVrRW/7tpnWqk8wEXugUFBREX0ngnB7w9Lkm9N+r1fLlcU+aNAkXDhmCOa5B8g9VpCmTvToOkv9ffht0+/btcs+1o3zCjlrZcm//qKeARu0wceJENGvWDB06dMDEiRODBjCGFW5fYhbmR6OLPDlKDbOGNmqpWAF5UFkoHo8Hd955J9q0aYO7Pt2H031GAWNeBMbMB87p7r9w+fs9evRoTduNWo16kGCC6/IHIU1Z7pslLSrld4dKisOXJqyUbhf73YL/aG/kQNbhdOGOO+7A+6da4OPfNX6mel3h++fpU+GDuFmzZiHv2uv8nvOO9fj5qMpU6PVbBD01ePDgsNt46w3/Ul5uHXuMA320crniUfl5nhNNx5P/Z6Nui7b+fz57Ahh0s/zvMmOmitfN1Q/7/ul2e3SbFbBG4/KBoeVjU84991w4c++CpBhfUCPTv4PAZrNBEAQ8+eSTmrax5/fdOFFyQpf2xkvKBMirVq1Cx44dkZOTg6eeeirRzdHssX99GrJnzuX24PlXX0ObNm0wcOBALP94NTZs2oyJEyeGHFkuCAKcNwdMOVstTE/iRZPkYuReY18G7lsJR2ZNPPjggyFfJooiHpo2zf9Jt1ueZjJQtdrYd/0rWN31Lkj3rgDuWwm3BHy5+wQ2HAUmTpzoN+pWFEV8+OGH8qCjCBUEvKRqdTB58mSIooj8/Hz0798fvXr1wrPPPut/e89kgiRJWLBgAXr16uXLvc3Pz8fy5csVi5nw44/ay/cAUN93b/vKAz3vhc4FF1xQkdcGwG3JwsZBM4B7A67IG7RU75ls2QUAsHr1atSvXx/9+/fH1KlTsX57Rc9NVl2NNVfNFuDuf8v51TXr+5U0++n77/xmnHv22WfRq1cvDB48GNOnT8fgwYNx9dVXY53KFLURtewq55KH0vNySJnVMGfOHCxYsABfffV19NsYfpecqz55Gdw5F+Cdd96Bu8NgwJvbq6wzevNcoG5THDp0CDu73yyfe9EMMKtZL/r26eDMcQ3593W09ZK6nOFrbrtcLvzuqBa27B0AOfWgXjMs+fd/NG03atVqATe/CJzbT35cK/bJj2KpgBGVMPWpVZXfzYjK0IqZBUsi3C2w2+34cp9/4O3tTdfK3T18bW63ueIC9vstRfDcHFzpQC9S+cXRK3Mer7igVd7hCzTYv4ybKeDiUa49reC92wSopzN50/CSgd/3lYTXXnutUr3IoiiiV69e+NhdnkZy6jguvvhi/LZ3P9B5KHBVRYWkGtbg3ynvZFNaLHnrdZw5o34BsvuXn1SfTzSTZGitHn243W506NABn332GVq2bIm+ffvi3Xff9Z8PXqFPnz4oKgoeFGSkqVOnyr1fAHqueRhbh5WXFPrxS+DjZ9GgQQM0adIEWVlZ2LNnD0pKSuQBYq26A/OukX/QvcHiVwXAxmUwmUywWCwwm83IzMzE6dPlJ5fGoDKi5yvyzrzpBn6jdmtly6NTvdYtAeo195XPinY7Fotcc/WMwy0PnpoUZrDKkV2+aX4BALs2AR/OgclVCqnf9cBvG4G+1wDH9wPiu/Ic8X2vAY7tAz6dB9zwjPya9x/1X6/3vXs+Tx6MMeGtiO32veb08eAvy2P75CD3rTvkfwdSO1Zul6aZ21BwN9DjMvlW4NtTgCO/yb3Z2eWjuYv3AtmVKwnl88Fs4Oge4EwJcKdiNqRTxUD+LYDtBrm2cqTAKVriu8DhX+Teebcr/MVeKD/+DzhPvVygqjcnAbe8Gv12vMdaT0X/Dd8zvfguOUfygsjVNirln1OAP37T/t3y5xGgTiPg4E9AM413YhLlj9+AxgG1hZ/PA+5cEnXVkSB7twGtgku1hbXtU+D7z+XvKCO8cBXwl6n+vaxq312VcaYkYLbOAC+OBCYv02dbB36UA+JDO6PKB/ZxnAGsiuO85UO/Hnm/Y7hhGdAvfFWgpPHyDUDZGZjNJnTv3h0DBgxAnTp1UFBQgCNHjsDj8cBkMiEjIwNZWVlwOBzBdwFNZrnjxGv7Glg+nw93vRbyb43ivLGcPAJ3eYWVuhv/ibYnf8ahQ4dQVlaG47cs1tbmU8fUB5W//ygw8EaYz57A33PO4umnnw5exkChYsaUCJBFUcQjjzyCTz/9FIA8AA1AyCuXeAfIU6dOxZzla4Erygd1LZkqF1YHgCO7gcLyH+PqdeQBVSUH5QoEeYoe2hVPyHlRXmdKgPX/AYbeBuxcC/yxS77SrVUf6Hutfo3fXgh0yQWWPQw07ygHAOGCjUM/A02jnDHpp6+Bk0flW92FC+QSOrFylQX32PzvDWDIOPXll0yVb4OeOCTnnnnzzvZ8K+ebeWcgVPPhHGDg/0UfFH38nPyl3K4v0P2S4L9LnthuGRMRESmJ7wK/b5Ur/thuAL54DTihGAh6Tg/5dwwAdoryb2jD1sCJP4CcgMmPAi98Thz2jU/wu9A4+jvwgwDs3yH/Xa/c62P7gLfuwAMPPBDXIDmlA+Rly5Zh1apVeP11Oe/p7bffxvr16/HSSy+pLh/vANlkMunXq0tERERU1ZTfcc/MzJTrUsdJqJgxbcq85efn+waDHTp0CAcOHIhvA969X84b/fOonPSffQ7QfiCwbin8BuLUrA+UnpTzeWvWA1p0lq/kin8H2vSWl61WSz5RzBb5ud82yoOWTACq15VvbZ48KvcoW6sDZ/+U8z1r1pd7a8/tC+zbLvd8uhxyr/WBH+Ue3AM/Ag1ayK8pOShfBZ7bX+5hrdUQqJ0tt61BS+DobsDjkrfVsI3c83lkN9Csg7zs8f1yqkBmNbldxb/L7Sg5COwqkm9rNmoL/PwN4CiVe9Bd5bd46jSW96ltb/mq0e0Ejh+QRxTXqAcc3gmcnwfs/R44ugto1E5+/dHf5fI8f/4hv6ZNL7mnvZNdfs+/WiynhtRtLA+e+XWjfIXrdsr//+M3+f11OQG3Q36+VTe5yPn3nwPZrQGzGXCWASePyH87tFNOK9m7rbzqgAko3iOnN5QclPehVgM53/XQL8D+7fLrm7aX37+yM/J71Kwj8PsW+fa0JQPoNES+hbV/h/y+eTxyG4t/l98HZ/l71ckObFoh33UoPSWfF7UbyutqnANkZsn7fPqY3DPgLAP++FVuq9sp/7/5eXIKQ4ZV3n69ZvJ5VLsRsGerfFz7XC2npWS3ktM3yk7L77fFIi9Xckg+B+o3Bw78IN9JcJbK+12vmbytjCz5tRmZ8n5lZgEtusjnUtu+QHZLYM93wL7v5X0+c0K+zV16Wv5/hlXOAyw9JQ+5z6wmD0YsOSRvI8cG/LBGfv7YfrlHo3lHeZ+P7ZPX1zRHPg7e9TVqK7fbnCH3kJw+Lu+7OUNeR+2GcipJjbryv3eKcu9/9Trye3zoZ/k8KDkI9Lse+GUd4DgNnDout9VxRt7G2ZPyeVByUD5n2vaW38N6zeW2/HkEOHVUPr+bdpDfr4M/y5+JkoPy90WDFvKxqF4H+HW9/NksPSkPwqteR77zcHSPfA5n1ZBTkaw15GPw20b5XPl9q/y+l52Wj1u1WvL7ZzLJ3xcNW5eXvyuTP9cNWgDffiJ/zq3V5fe27BRw5k95WYtF3ldvG1p0kt/fDKv8nXP6uHyu79sut8eSKX+3HdsHtO4lt6N+C3m9e7fJ35O/bQDa9ZO/w35dL7/3rbrJ773ZDFSvJ7e7dU9g9yb5nDmnh3weH/1d/vz9eURuy4k/5ON2+Bf5vcyqJb/HNerK/z/ym/weOUvlc8icIaeGVK8tr+8HAahT/t1Qq4G87OljQN2m8vLV68jnjckkfz5adpW/L+s0ltd18oh8rpot8rFr2r7i3DOZ5XNj3/fyv08elc/Fpu3lc89kko99x8HA1o/k96nstPyZtVYvP87laUeuMqBRG/mzcuAH+XOaVVP+7B/fL3+nHz8gf4dUqyV/hxz9Xf6+6nqR/P5bMuS2WzLl35ga9eTlSg7KbXaWyedOu37y9vfvkN8HV5m8DxlZ8n6eOQGcN1h+XL02UK2OvL8HfpDfl1PF8n91GsvHrm4T+XPU7Dx5nWaz/D5aMoFjewFrTXl/Dv4kr9NVJo/5OPyLXKbx0E6g8bny+9emV/lnd6+8n6dL5P//+Yd8N9TtlL+Djv4urzOzmty27YVyO0wW+bP5+1b5WDRqI38+GrSQ/2/JkM+LMyfk9/f0cfk9KDkob6Nes/L3oET+96ljcntPHpFfU7uhfG5WqyW/9216ya+1ZMq/BaeOlh/XmnJo0LyjvA8ZVrl9uzfL33/NOsi/q6Un5fO9dmN5PTXryeXYsmrIvymbV1b8VmRkyueZ9zEgn2MdB8vfEeuWyJ9Zs0VuT92mgLWa/NtgrSF/T2fVrBgXU7xH3sezJ+Xzq3a2fExLDsq/V2f/lL9LM6vJ2/3zD3kfThyWt1N2Wo4lThyW2/bnEfm9h0k+by0ZwPefydvPqiF/FiEPKo17DKciJXqQkz3FInAQABERERFFr1OnThFnpNRTSvcg9+3bFzt37sSuXbvQokULLFmyBP/6178S3SwfSZIYJBNVMWaz2fgKCTHy1hl3u91RTZUbb6byqjMUnneAs9vt9h1TtUoYZrMZGRkZkCTJV9ot3DolSYIkSWjYsCE6deqE33//3TdJxNmzZ+WayiYT3G43TCYTrFYrSlVKVeqxf8r9MZlMMJvNvt/WrCx53ElpaWnQZ847XbskSb7PpCRJyMjIQPXq1XH69Gm/11itVnTu3Bl16tTB77//jpMnT/pqqautP1R7vdsxmUw477zzcObMGRw5csS3Du+x8B4ztXPdewy82wz3nVJVPivxDo7DSYkAOSMjAy+99BJGjBgBt9uNcePGoUuXLolulp90PXEPHDiA5s2bJ7oZpAGPVWrgcUodPFapg8cqdaTKsUqJABkALrvssugnlyAiIiIiihJrTRERERERKTBAJiIiIiJSYIBMRERERKTAAJmIiIiISIEBMhERERGRAgNkIiIiIiIFBshERERERAoMkImIiIiIFBggExEREREpMEAmIiIiIlJggExEREREpMAAmYiIiIhIwSRJkpToRuitYcOGaNOmTaKbkRaOHDmCRo0aJboZpAGPVWrgcUodPFapg8cqdSTbsdq9ezeOHj0a9HxaBsiknz59+qCoqCjRzSANeKxSA49T6uCxSh08VqkjVY4VUyyIiIiIiBQYIBMRERERKTBAprAmTJiQ6CaQRjxWqYHHKXXwWKUOHqvUkSrHijnIREREREQK7EEmIiIiIlJggExEREREpMAAuYrZu3cvhg4dis6dO6NLly6YN28eAODYsWMYPnw42rdvj+HDh+P48eMAAEmSMHnyZOTk5KB79+7YvHkzAGDr1q2w2Wzo0qULunfvjqVLlyZsn9KVXscKAPbs2YOLL74YnTp1QufOnbF79+5E7FLaivZY/fjjj7DZbMjKysKzzz7rt65Vq1ahY8eOyMnJwVNPPRX3fUlneh4nAHC73ejVqxeuuOKKuO5HVaDnsXrhhRfQpUsXdO3aFTfccANKS0vjvj/pLNpj9c4776B79+7o1q0bBg4ciG+//TbsehJGoirlwIED0qZNmyRJkqQ///xTat++vbR9+3bp/vvvl2bPni1JkiTNnj1beuCBByRJkqSPPvpIuuSSSySPxyOJoij169dPkiRJ+umnn6Sff/5ZkiRJ2r9/v9S0aVPp+PHj8d+hNKbXsZIkSRoyZIi0evVqSZIk6eTJk9Lp06fjvDfpLdpjdfjwYWnDhg3StGnTpGeeeca3HpfLJbVr10769ddfpbKyMql79+7S9u3b479DaUqv4+T13HPPSTfccIN0+eWXx28nqgi9jtW+ffukNm3aSGfOnJEkSZKuu+466c0334zvzqS5aI/VN998Ix07dkySJEn6+OOPfb9VodaTKOxBrmKaNWuG888/HwBQu3ZtdOrUCfv378eKFSswduxYAMDYsWOxfPlyAMCKFSswZswYmEwmDBgwACUlJTh48CA6dOiA9u3bAwCaN2+Oxo0b48iRIwnZp3Sl17HasWMHXC4Xhg8fDgCoVasWatSokZB9SlfRHqvGjRujb9++yMzM9FvPhg0bkJOTg3bt2sFqtWL06NFYsWJFXPclnel1nABg3759+Oijj3DrrbfGrf1ViZ7HyuVy4ezZs3C5XDhz5gyaN28et/2oCqI9VgMHDkT9+vUBAAMGDMC+ffvCridRGCBXYbt378aWLVvQv39/HD58GM2aNQMANG3aFIcPHwYA7N+/H61atfK9pmXLlkEn7IYNG+BwOHDuuefGr/FVTGWO1c8//4x69erhmmuuQa9evXD//ffD7XYnZD+qAi3HKhQtnzfSR2WOEwBMmTIFc+bMgdnMn1GjVeZYtWjRAn//+99xzjnnoFmzZqhbty4uvvjieDS7Sor2WC1atAiXXnpp2PUkCj/ZVdSpU6dw7bXXYu7cuahTp47f30wmE0wmk6b1HDx4EDfffDPefPNN/lAYpLLHyuVy4auvvsKzzz6LjRs34rfffsNbb71lYIurLr0+V2Ssyh6nDz/8EI0bN0bv3r2NbCah8sfq+PHjWLFiBXbt2oUDBw7g9OnT+Oc//2lkk6usaI/VF198gUWLFuHpp5/WvJ54YkRTBTmdTlx77bW48cYbcc011wAAmjRpgoMHDwKQg97GjRsDkK++9+7d63vtvn370KJFCwDAn3/+icsvvxxPPPEEBgwYEOe9qBr0OFYtW7ZEz5490a5dO2RkZOCqq67yG8BH+ojmWIUS7vNG+tDjOH3zzTdYuXIl2rRpg9GjR2PNmjW46aabDG97VaPHsfr888/Rtm1bNGrUCJmZmbjmmmuwdu1aw9te1UR7rL777jvceuutWLFiBbKzs8OuJ1EYIFcxkiRh/Pjx6NSpE+677z7f83l5eVi8eDEAYPHixbjyyit9zxcUFECSJKxbtw5169ZFs2bN4HA4cPXVV2PMmDEYOXJkQvYl3el1rPr27YuSkhJfjviaNWvQuXPn+O9QGov2WIXSt29f7Ny5E7t27YLD4cCSJUuQl5dnaNurEr2O0+zZs7Fv3z7s3r0bS5YswbBhw9grqTO9jtU555yDdevW4cyZM5AkCYWFhejUqZOhba9qoj1We/bswTXXXIO3334bHTp0iLiehEnU6EBKjK+++koCIHXr1k3q0aOH1KNHD+mjjz6Sjh49Kg0bNkzKycmRcnNzpeLiYkmSJMnj8Uh33HGH1K5dO6lr167Sxo0bJUmSpLffflvKyMjwraNHjx7Sli1bErhn6UevYyVJkrR69WqpW7duUteuXaWxY8dKZWVlidqttBTtsTp48KDUokULqXbt2lLdunWlFi1aSCdOnJAkSa5G0r59e6ldu3bSrFmzErlbaUfP4+T1xRdfsIqFAfQ8Vg8//LDUsWNHqUuXLtJNN90klZaWJnLX0k60x2r8+PFSvXr1fMv27t077HoShVNNExEREREpMMWCiIiIiEiBATIRERERkQIDZCIiIiIiBQbIREREREQKDJCJiIiIiBQYIBMRpblHHnkEzz77bKKbQUSUMhggExEREREpMEAmIkpDTzzxBDp06IBBgwbhp59+AgC8+OKL6Ny5M7p3747Ro0cnuIVERMkrI9ENICIifW3atAlLlizB1q1b4XK5cP7556N379546qmnsGvXLmRlZaGkpCTRzSQiSlrsQSYiSjNfffUVrr76atSoUQN16tRBXl4eAKB79+648cYb8c9//hMZGewfISIKhQEyEVEV8dFHH+HOO+/E5s2b0bdvX7hcrkQ3iYgoKTFAJiJKMxdeeCGWL1+Os2fP4uTJk/jggw/g8Xiwd+9eDB06FE8//TROnDiBU6dOJbqpRERJiffYiIjSzPnnn49Ro0ahR48eaNy4Mfr27QuTyYSbbroJJ06cgCRJmDx5MurVq5fophIRJSWTJElSohtBRERERJQsmGJBRERERKTAAJmIiIiISIEBMhERERGRAgNkIiIiIiIFBshERERERAoMkImIiIiIFBggExEREREp/D+XGXxASYOXjgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 720x432 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "#future= model.make_future_dataframe(periods=14)\n",
    "#forecast=model.predict(future)\n",
    "future_data = model.make_future_dataframe(periods=14)\n",
    "#forecast the data for Test  data\n",
    "forecast_data = model.predict(x_test)\n",
    "model.plot(forecast_data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b3c27ae6",
   "metadata": {
    "_cell_guid": "891d562f-af33-4a1a-aeca-52f3fb63e8a0",
    "_uuid": "301a637f-2bd9-49ab-880e-0161bf10de46",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:34.026784Z",
     "iopub.status.busy": "2022-05-01T20:48:34.026219Z",
     "iopub.status.idle": "2022-05-01T20:48:34.038190Z",
     "shell.execute_reply": "2022-05-01T20:48:34.037472Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.043656,
     "end_time": "2022-05-01T20:48:34.040114",
     "exception": false,
     "start_time": "2022-05-01T20:48:33.996458",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([4, 4, 4, ..., 4, 4, 4])"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "## Label encode the text\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "# creating instance of labelencoder\n",
    "labelencoder = LabelEncoder()#one hot encode the categores from label encoder\n",
    "# using the encoder to encode the categorical columns\n",
    "Y= labelencoder.fit_transform(target)\n",
    "Y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "041bb73f",
   "metadata": {
    "_cell_guid": "047d8e4f-bee4-40bb-8935-2556174c8b40",
    "_uuid": "7485bb7b-cc65-4567-ab2a-90bbaf1feb69",
    "collapsed": false,
    "execution": {
     "iopub.execute_input": "2022-05-01T20:48:34.099381Z",
     "iopub.status.busy": "2022-05-01T20:48:34.098825Z",
     "iopub.status.idle": "2022-05-01T20:48:34.106984Z",
     "shell.execute_reply": "2022-05-01T20:48:34.106132Z"
    },
    "jupyter": {
     "outputs_hidden": false
    },
    "papermill": {
     "duration": 0.040085,
     "end_time": "2022-05-01T20:48:34.108939",
     "exception": false,
     "start_time": "2022-05-01T20:48:34.068854",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['No Report', 'No Report', 'No Report', ..., 'No Report',\n",
       "       'No Report', 'Local Outbreak'], dtype=object)"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "preds = outbreak.predict(forecast_data.yhat.array.reshape(-1, 1))\n",
    "y2=labelencoder.inverse_transform(preds)\n",
    "y2"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.12"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 34.760704,
   "end_time": "2022-05-01T20:48:34.957778",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2022-05-01T20:48:00.197074",
   "version": "2.3.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
