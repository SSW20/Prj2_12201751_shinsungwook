import pandas as pd
df = pd.read_csv('2019_kbo_for_kaggle_v2.csv')

pd.set_option('display.max_rows', 10)
years = [2015, 2016, 2017, 2018]
for year in years:
    print(f"{year}년 상위 10명 선수:")
    subset_df = df[df['year'] == year]
    hits10 = subset_df.nlargest(10, 'H')[['batter_name', 'H']]
    avg10 = subset_df.nlargest(10, 'avg')[['batter_name', 'avg']]
    hr10 = subset_df.nlargest(10, 'HR')[['batter_name', 'HR']]
    obp10 = subset_df.nlargest(10, 'OBP')[['batter_name', 'OBP']]
    
    print(f"안타 상위 10명:\n{hits10}")
    print(f"타율 상위 10명:\n{avg10}")
    print(f"홈런 상위 10명:\n{hr10}")
    print(f"출루율 상위 10명:\n{obp10}")
pd.reset_option('display.max_rows')
maxWarPosition = df[df['year'] == 2018].groupby('cp')['war'].idxmax()
player = df.loc[maxWarPosition][['cp', 'batter_name', 'war']]
print("\n2018년에 각 포지션별로 승리 기여도가 가장 높은 선수:\n", player)

cols = ['age', 'G', 'PA', 'AB', 'R', 'H', '2B', '3B', 'HR', 'RBI', 'SB', 'CS', 'BB', 'HBP', 'SO', 'GDP', 'fly', 'war']
correlations = df[cols + ['salary']].corr()['salary']
correlationsMax = correlations[:-1].idxmax()
print(f"\n연봉과 가장 높은 상관관계를 가진 특성: {correlationsMax} - {correlations[correlationsMax]:.2f}")
