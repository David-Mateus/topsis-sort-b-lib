# Topsis Sort B - LIB PYPI

 The TOPSIS-Sort-B is an enhanced variation of the TOPSIS-Sort method, designed to address classification and sorting problems in multiple criteria decision-making. In this method, boundary profiles are employed to determine categorization classes and to sort alternatives based on the proximity of their proximity coefficients to the established profiles.

## Tecnologias usads
| Tecnologias | Versão  | Install                               |
|-------------|---------|---------------------------------------|
| Python      | 3.12.1  | `pip install python==3.12.1`          |
| Numpy       | 1.26.4  | `pip install numpy==1.26.4`           |
| Pandas      | 2.2.1   | `pip install pandas==2.2.1`           |


## Installtion
1. Install the required dependencies by running the following command: pip `pip install topsisSortLib`
## How to Run the Application
1. After installing the package, import the library.
2. from topsisSortLib import topsis_b_sort_profile_classification

## How to Use
1. To utilize the topsis_b_sort_profile_classification function, follow these steps:
2. Import pandas: Begin by importing the pandas library as pd.
  # How to Use

To utilize the `topsis_b_sort_profile_classification` function, follow these steps:

1. **Import pandas**: Begin by importing the pandas library.

    ```python
    import pandas as pd
    ```

2. **Load CSV File**: Load your CSV file into a pandas DataFrame using `pd.read_csv()`.

    ```python
    df = pd.read_csv('your_file.csv')
    ```

3. **Clean Data**: Clean the DataFrame by converting all non-numeric values to numeric using `pd.to_numeric()` and filling any missing values with zero.

    ```python
    df = df.apply(pd.to_numeric, errors='coerce').fillna(0)
    ```

4. **Call Function**: Pass the cleaned DataFrame along with other necessary arguments into the `topsis_b_sort_profile_classification` function.

    ```python
    result = topsis_b_sort_profile_classification(
        decision_matrix=df,
        domain_matrix=your_domain_matrix,
        dominant_profiles=your_dominant_profiles,
        weights=your_weights
    )
    ```

Make sure to replace `your_file.csv`, `your_domain_matrix`, `your_dominant_profiles`, and `your_weights` with the appropriate variables or data structures.

  `
## References

- Silva, D. F. L., & Filho, A. T. A. (2020). Sorting with TOPSIS through boundary and characteristic profiles. Journal Name, Volume(1), 141.
- GeeksforGeeks.TOPSIS method for Multiple-Criteria Decision Making (MCDM). Retrieved from [[URL](https://www.geeksforgeeks.org/topsis-method-for-multiple-criteria-decision-making-mcdm/)]

## Deploy
- Aplicação
- library [[URL](https://pypi.org/project/topsisSortLib/)]