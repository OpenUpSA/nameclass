# nameclass
A simple API to classify race and gender by name. 

This tool attempts to infer a person's race and gender from their name using a classification algorithm. Attempting to identify a person's race from their name may seem ethically questional but is important for analysis of racial transformation over time. This classifier was trained using data from South Africa and so may not easily be used for other countries. Race classes are borrowed from official races used in South Africa for classification of demographics.

The classifier tends to work well with African and Chinese names and to a lesser extent with Indian names. Coloured names are often confused with both White and Indian names resulting in poor performance for the class.

5-fold crossvalidation results are shown below:

<table>
    <tr>
        <th>Train size</th>
        <th>Test size</th>
        <th>Race</th>
        <th>Precision</th>
        <th>Recall</th>
        <th>F1</th>
    </tr>
    <tr>
        <td>4000</td><td>500</td><td>White</td><td>0.7832</td><td>0.7666</td><td>0.7748</td>
    </tr>
    <tr>
        <td>4000</td><td>500</td><td>Indian</td><td>0.9092</td><td>0.8173</td><td>0.8608</td>
    </tr>
    <tr>
        <td>4000</td><td>500</td><td>Coloured</td><td>0.6556</td><td>0.7423</td><td>0.6962</td>
    </tr>
    <tr>
        <td>4000</td><td>500</td><td>Chinese</td><td>0</td><td>0.0</td><td>0</td>
    </tr>
    <tr>
        <td>4000</td><td>500</td><td>African</td><td>0.9152</td><td>0.9845</td><td>0.9485</td>
    </tr>

<table>
    <tr>
        <th>Train size</th>
        <th>Test size</th>
        <th>Race</th>
        <th>Precision</th>
        <th>Recall</th>
        <th>F1</th>
    </tr>
    <tr>
        <td>3000</td><td>1500</td><td>White</td><td>0.768</td><td>0.7459</td><td>0.7567</td>
    <tr>
        <td>3000</td><td>1500</td><td>Indian</td><td>0.8885</td><td>0.8234</td><td>0.8547</td>
    </tr>
    <tr>
        <td>3000</td><td>1500</td><td>African</td><td>0.9136</td><td>0.9839</td><td>0.9474</td>
    </tr>
    <tr>
        <td>3000</td><td>1500</td><td>Chinese</td><td>0.9629</td><td>0.3030</td><td>0.4609</td>
    </tr>
    <tr>
        <td>3000</td><td>1500</td><td>Coloured</td><td>0.6438</td><td>0.7280</td><td>0.6833</td>
    </tr>
</table>
</table>
