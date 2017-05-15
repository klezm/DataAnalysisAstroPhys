import pandas
import numpy
from io import StringIO
import matplotlib.pyplot as plt

#TASKS
T_1_2 = True
T_1_3 = True
T_1_4 = True
T_1_5 = True
T_1_6 = True

T_2_2 = True


if T_1_2:

    # 2. The dataset "cdbrfss1999.csv" contains 159989 entries.
    #     2.1. Take a sample of 20000 from this dataset and export it to an ASCII file. Make sure that your method
    #     allows to draw more than one sample from the population.  [10 points]
    #
    #     2.2.  Discuss your method to do so. Is your sampling a "good sample" in the sense that it is representative for
    #     the larger "population"?  [5 points]

    # to run as module if imported otherwise as script
    # def function():
    #     print("This is a module function")
    #
    # if __name__=="__main__":
    #     print("This is a script")

    # with open('cdbrfss1999.csv') as csvImport:                            # opens file (, 'rb' -> r=read b=binary)
    csvImport = "cdbrfss1999.csv"
    rows = sum( 1 for row in open( csvImport ))                             # counts lines
    import_size = 20000                                                     # sample size
    # skip = sorted(random.sample(range(1, rows + 1), rows - import_size))    # creates a list of skipped lines (without header)

    # random generator based on random function of numpy
    rand_sample = [0]
    rand_counter = import_size
    while rand_counter > 0:
        rand_nr = numpy.random.random_integers( 1, rows )
        if rand_nr in rand_sample:
            continue
        else:
            rand_sample.append( rand_nr )
            rand_counter -= 1
    choose_rows = sorted( rand_sample )
    # # print( 'chosen rows: %s' % choose_rows )
    # skip_rows = list( range( 0, rows ))
    # # print(len(skip_rows))
    # # print(skip_rows[0] , "<->" , skip_rows[-1])
    # # print("{0} <-> {1}".format(skip_rows[0], skip_rows[-1]))
    # for item in choose_rows:
    #     skip_rows.remove( item )
    # print( skip_rows )

    if input( "do you want to generate a sample of {0} samples? (y/n) ".format( import_size ) ) == "y":
        print("creating the data for task one can take some minutes.")
        lines = pandas.read_csv( open(csvImport), skiprows = lambda x: x not in choose_rows )
        # sample_out = open( 'sample.txt', 'w' )
        lines.to_csv( 'sample.csv', header = True, index = False )

    print('''\n
    2.1
    csv sample.csv created \n 
    \n''')

    print('''\n
    2.2.
    We wrote a sampling method using the random generator provided by numpy, which gives us a good sample of the
    population. The Generator generates a number between the second row (excluding the header) and  the number of rows
    and adds it to a list if the number isnt inside the list already. the list is completed if there are as many members
    inside the list as declared in import_size
    \n''')


if T_1_3:

    # 3. Each case in the the dataset can have up to 241 variables. Each one of these variables corresponds to a question
    # that was asked in the survey. For example, for genhlth, respondents were asked to evaluate their general health,
    # responding either excellent, very good, good, fair or poor. The exerany variable indicates whether the
    # respondent exercised in the past month (1) or did not (0). Likewise, hlthplan indicates whether the respondent
    # had some form of health coverage (1) or did not (0). The smoke100 variable indicates whether the respondent
    # had smoked at least 100 cigarettes in her lifetime. The other variables record the respondent’s height in inches
    # (hti) and feet (htf), weight in pounds as well as their desired weight, wtdesire, age in years, and gender.

    # 3.1. Locate the columns corresponding to the variables genhlth, exerany, htf, hti, smoke100, height, weight,
    # wtdesire, age, and sex.  [2 points]

    choose_sample_path = input("input your sample CSV (simply press enter for default: sample.csv): ")
    if  choose_sample_path == "":
        sample_csv_path = "sample.csv"
    else:
        sample_csv_path = choose_sample_path

    if input( "do you want to filter the samples? (y/n) ") == "y":
        # opening the csv via pandas and calculating the height and adding it to the csv
        sample_csv_usecols = ["GENHLTH", "EXERANY", "HTF", "HTI", "SMOKE100", "WEIGHT", "WTDESIRE", "AGE", "SEX"]
        sample_csv = pandas.read_csv( open( sample_csv_path ), header = 0, usecols = sample_csv_usecols )
        # print(sample_csv._AXIS_NAMES)
        sample_csv["HEIGHT"] = sample_csv.apply( lambda x: ( x["HTF"] * 12 + x["HTI"] ), axis = 1 )
        # print(sample_csv.axes[1])
        sample_csv.to_csv( 'sample_filter.csv', header = True, index = False )

        print('''
        3.2
        csv sample_filter.csv created including the calculated height in inch 
        ''')


    # 3.3. How many cases and how many variables are there in your sample?  [2 points]
    # (a) 9 cases; 20,000 variables
    # (b) 8 cases; 20,000 variables
    # (c) 20,000 cases; 9 variables
    # (d) 159,989 cases; 10 variables

    # 3.4. What type of variable is genhlth? [2 points]
    # (a) numerical, continuous
    # (b) numerical, discrete
    # (c) categorical (not ordinal)
    # (d) categorical, ordinal

    # http://www.dummies.com/education/math/statistics/types-of-statistical-data-numerical-categorical-and-ordinal/
    # https://www.bwl24.net/blog/2008/06/27/nominal-ordinal-und-metrisch-kleine-ubersicht-uber-die-datentypen-der-statistik/
    # https://www.ma.utexas.edu/users/mks/statmistakes/ordinal.html


    # 3.5. What type of variable is weight? [2 points]
    # (a) numerical, continuous
    # (b) numerical, discrete
    # (c) categorical (not ordinal)
    # (d) categorical, ordinal

    # https://en.wikipedia.org/wiki/Continuous_and_discrete_variables
    # http://www.statisticshowto.com/discrete-vs-continuous-variables/
    # http://www.henry.k12.ga.us/ugh/apstat/chapternotes/7supplement.html


    # 3.6. What type of variable is smoke100? [2 points]
    # (a) numerical, continuous
    # (b) numerical, discrete
    # (c) categorical (not ordinal)
    # (d) categorical, ordinal


    print('''
    3.3
    -> (c) 20,000 cases; 9 variables
    since we have 20,000 rows with 9 variables each
    
    3.4
    -> (d) categorical, ordinal
    since we have data thats not mathematically processable, even though the data can contain numbers. But the data can
    be ordered so its ordinal
    
    3.5
    -> (a) numerical, continuous
    since the data is measured and not counted its continuous
    
    3.6
    -> (c) categorical (not ordinal)
    this variable indicates if a event occured so it is categorial and since its just 0 or 1 its not ordinal
    ''')

if T_1_4:
    # 4. Take all genhlth entries from your sample and draw a bar chart to visualize how the cases are distributed across
    # the possible categories.  [5 points]

    genhlth_col = pandas.read_csv( open( 'sample_filter.csv' ), usecols = ['GENHLTH'] )#, header = 0, index_col = 0 )
    # print( genhlth_col[[ "GENHLTH" ]] )
    # print(type(genhlth_col))                                  # outputs <class 'pandas.core.frame.DataFrame'>
    # genhlth_col['GENHLTH'].value_counts()
    genhlth_col_count = genhlth_col['GENHLTH'].value_counts().sort_index()      # sums up all different variables +sorts
    # print(type(genhlth_col_count))                            # outputs <class 'pandas.core.series.Series'>
    # print(genhlth_col_count)

    # genhlth_col = genhlth_col.values
    # # print(genhlth_col.tolist())
    # genhlth_col_ls = [val for sublist in genhlth_col.tolist() for val in sublist]
    # # print(genhlth_col_ls)

    # creating a plot for fig1
    plt.bar( genhlth_col_count.index, genhlth_col_count )
    plt.xticks(list(genhlth_col_count.index))
    plt.xlabel("general health")
    plt.ylabel("# of people")
    plt.title("distribution of health self-appraisal")
    plt.savefig('fig1.png')                                     # first save, then show
    plt.show()

    print('''
    4.
    the output was created as fig1.png
    ''')

if T_1_5:
    # 5.  Combine the smoke100 with the  genhlth entries from your sample and draw TWO bar charts, one showing
    # the health of the smokers and a second one showing the health of the non-smokers.  [5 points]

    hlt_smk_df = pandas.read_csv( open( 'sample_filter.csv' ), usecols = ['GENHLTH', 'SMOKE100'] )
    hlt_nsmk = pandas.DataFrame()                                           # creating empty pandas DataFrame
    hlt_ysmk = pandas.DataFrame()
    for i in hlt_smk_df.values:                                             # splitting the frame into non-s / smokers
        if i[1] == 1:
            x = [i[0]]
            # hlt_nsmk.append(i[0])
            hlt_nsmk = hlt_nsmk.append(pandas.DataFrame({"GENHLTH": x}))
        else:
            y = [i[0]]
            # hlt_ysmk.append(i[0])
            hlt_ysmk = hlt_ysmk.append(pandas.DataFrame({"GENHLTH": y}))

    # hlt_nsmk['GENHLTH'].value_counts()
    # hlt_ysmk['GENHLTH'].value_counts()
    hlt_nsmk_count = hlt_nsmk['GENHLTH'].value_counts().sort_index()        # sums up variables and sorts them
    hlt_ysmk_count = hlt_ysmk['GENHLTH'].value_counts().sort_index()

    # print(hlt_nsmk_count)
    # print(hlt_ysmk_count)
    # print(list(hlt_nsmk_count.index))
    # print(list(hlt_ysmk_count.index))

    # print(sorted(set(hlt_nsmk)))
    # print(hlt_nsmk.count())

    # plotting two graphs into one plot
    # https://chrisalbon.com/python/matplotlib_grouped_bar_plot.html
    hlt_smk_plt = plt.subplot(111)
    hlt_smk_plt.bar(hlt_nsmk_count.index - 0.15, hlt_nsmk_count, width=0.3, alpha=0.5, color='#EE3224', align='center')
    hlt_smk_plt.bar(hlt_ysmk_count.index + 0.15, hlt_ysmk_count, width=0.3, alpha=0.5, color='#F78F1E', align='center')
    hlt_smk_plt.legend(['non smokers', 'smokers'], loc='upper right')
    hlt_smk_plt.set_xticks(list(hlt_nsmk_count.index))                  # xticks needs a list
    # plt.ylim( [ 0, max( hlt_nsmk_count[ : ] + hlt_ysmk_count[ : ] ) ] )
    hlt_smk_plt.set_xlabel('health condition')
    hlt_smk_plt.set_ylabel('# of people')
    plt.title("health self appraisal of smoker and none smokers")
    plt.savefig('fig2.png')
    plt.show()

    print('''
    5.
    the output was created as fig2.png
    ''')

if T_1_6:
    # 6. Next let’s consider a new variable bmi that doesn’t show up directly in this data set: Body Mass Index (BMI).
    # BMI is a weight to height ratio and can be calculated as.
    # BMI = ( weight(lb) / height(in)^2 ) * 703         according to wiki -> ^2
    # (703 is the approximate conversion factor to change units from metric (meters and kilograms) to imperial
    # (inches and pounds). Compute the bmi for each case in your sample and add it to the sample (e.g. as additional
    # column).  Visualize the distribution of the BMI in your sample. ATTENTION: Remember, that the height was
    # given in feet and inches seperately. make sure to compute the total height in inches! [10 points]

    sample_import = pandas.read_csv(open('sample_filter.csv'))
    # creating a new column "BMI"
    sample_import["BMI"] = sample_import.apply(lambda x: ( x["WEIGHT"] / ( x["HEIGHT"] ** 2 ) * 703 ), axis = 1 )
    sample_import.to_csv('sample_filter_bmi.csv', header = True, index = True)

    sample_bmi = pandas.read_csv(open('sample_filter_bmi.csv'), header=0, usecols=[ "BMI" ] )
    sample_bmi_count = sample_bmi['BMI'].value_counts().sort_index()

    plt.bar(sample_bmi_count.index/3, sample_bmi_count)
    # plt.xticks(list(sample_bmi_count.index))
    plt.xlabel( "BMI" )
    plt.ylabel( "# of people" )
    plt.title("BMI distribution")
    plt.savefig('fig3.png')
    plt.show()

    print('''
    6.
    the output was created as fig3.png
    ''')

if T_2_2:
    # 2. Compare the median household  income for counties that gained population from 2000 to 2010 versus counties
    # that had no gain.  [6 Points]

    county_import = pandas.read_csv( open( 'county.txt' ) )
