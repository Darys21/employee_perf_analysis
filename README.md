
# Employee Performance Analysis Project

## 📌 Project Overview
This project focuses on analyzing employee performance and working hours within an organization to identify trends, disparities, and outliers. The goal is to uncover actionable insights to improve workforce efficiency and employee satisfaction. The dataset contains 311 employees with 36 variables, including both quantitative metrics (e.g., salary, engagement scores) and qualitative factors (e.g., performance scores, work-life balance).

---

## 🎯 Objectives
1. **Understand Distributions**: Analyze the distribution of performance scores and working hours.
2. **Identify Outliers**: Detect anomalies in employee performance or engagement.
3. **Key Insights**: Explore relationships between metrics like salary, satisfaction, and performance.
4. **Recommendations**: Provide actionable suggestions for organizational improvement.

---

## 📊 Dataset Overview
- **Source**: `HRDataset_v14.csv`
- **Size**: 311 rows × 36 columns
- **Key Variables**:
  - **Quantitative**: `Salary`, `EngagementSurvey`, `EmpSatisfaction`, `SpecialProjectsCount`, `Absences`
  - **Qualitative**: `PerformanceScore`, `WorkLifeBalance`, `Department`, `RecruitmentSource`
- **Data Cleaning**:
  - Dropped rows with missing `PerformanceScore`.

---

## 🔍 Key Findings

### 1. Performance Score Distribution
- **Most Common Score**: "Fully Meets" (observed in the majority of employees).
- **Outliers**: A small subset of employees scored "Exceeds" or "Needs Improvement," highlighting opportunities for recognition or training.
- **Visualization**:
  ```python
  sns.countplot(x='PerformanceScore', data=df, palette='viridis')
  plt.title("Distribution of Performance Scores")
  ```
  ![Performance Score Distribution](https://via.placeholder.com/600x400?text=Exceeds+vs+Fully+Meets)

### 2. Employee Satisfaction
- **Mean Satisfaction**: 3.89/5, indicating moderate satisfaction.
- **Variability**: Scores ranged from 1 (low) to 5 (high), with a standard deviation of 0.91.
- **Correlation**: Higher satisfaction linked to lower absenteeism and higher engagement scores.

### 3. Salary Analysis
- **Average Salary**: $69,020, with significant variation (standard deviation: $25,156).
- **Range**: $45,046 to $250,000, suggesting disparities that may require review (e.g., role-based equity checks).

### 4. Engagement Survey
- **Average Engagement**: 4.11/5, showing generally high engagement.
- **Low Engagement**: A subset of employees scored ≤3.02, indicating potential burnout or disengagement.

### 5. Departmental Trends
- **High Performers**: Employees in departments like `Engineering` and `Sales` showed higher performance scores.
- **Training Needs**: Departments with lower scores (e.g., `Operations`) may benefit from targeted development programs.

---

## 📈 Visualizations
1. **Performance Scores**: Bar plot showing frequency of each score category.
2. **Salary Distribution**: Histogram/KDE plot to visualize salary ranges and outliers.
3. **Engagement vs. Satisfaction**: Scatter plot to explore relationships between metrics.

---

## 🛠️ Tools & Libraries
- **Python**: pandas, matplotlib, seaborn, numpy
- **Data Cleaning**: Handling missing values, filtering irrelevant columns.
- **Analysis**: Descriptive statistics, correlation analysis.

---

## 🚀 Recommendations
1. **Recognition Programs**: Reward "Exceeds" performers to retain top talent.
2. **Targeted Training**: Address gaps for employees scoring "Needs Improvement."
3. **Salary Review**: Investigate disparities and align pay with role expectations.
4. **Engagement Initiatives**: Implement mentorship programs for employees with low engagement/satisfaction.
5. **Department-Specific Strategies**: Customize training for underperforming teams.

---

## 📂 How to Use This Project
1. **Prerequisites**:
   - Install Python libraries: `pandas`, `matplotlib`, `seaborn`.
   - Download `HRDataset_v14.csv` (ensure correct file path in the notebook).
2. **Run the Notebook**:
   - Execute cells sequentially to reproduce analyses and visualizations.
3. **Customize**:
   - Modify filters (e.g., focus on specific departments).
   - Add new visualizations (e.g., box plots for salary outliers).

---

## 🔗 Future Work
- **Predictive Modeling**: Use regression to predict performance based on engagement/salary.
- **Longitudinal Analysis**: Track changes in satisfaction over time.
- **Exit Interviews**: Analyze turnover reasons for employees with low satisfaction.

---

## 📝 Conclusion
This analysis reveals actionable insights into employee performance and engagement. By addressing outliers and leveraging strengths, the organization can foster a more productive and satisfied workforce. Further exploration of department-specific trends and predictive modeling could deepen these insights.

**Author**: [Your Name]  
**Date**: [Project Completion Date]  
**Contact**: [Your Email/LinkedIn]  

--- 

🔍 **Explore the Jupyter Notebook**: [`employee_perf.ipynb`](employee_perf.ipynb)  
📊 **Dataset**: [`HRDataset_v14.csv`](HRDataset_v14.csv)