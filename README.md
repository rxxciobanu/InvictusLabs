# Invictus Labs
![image-description](assets/logo_transparent.png)
## Description ##

The scope of Invictus Labs is to construct a platform for measuring the credit risk of DeFi (lending) pools. We achieve that by modelling the relationships between entities that partake in borrowing through causal inference and machine learning techniques. 

Sophisticated financial institutions in TradFi model various types of risks, such as credit, counterparty, market, political, country risks. 

In order to mitigate risk, there exist two well known techniques:

- qualitative - methods that do not require a model. Here, the risk is assesed using mostly expert-driven techniques.
- quantitative - mathematical models are used, allowing for more elaborate analysis.

The end goal is to measure the risk of default of any borrower as a function of his interaction with all the other borrowers he may have been exposed to. This means that we not only take into account data about the borrower as a standalone entity but also the ripple effects of the actions of all the other entities from the DeFi ecosystem.

To achieve this, we are constructing a quantitative engine made of 2 Models (Borrower and Borrower-to-Borrower), through which we create an Overall Credit Risk. The Borrower model will output the individual's credit risk, whereas the Borrower-to-Borrower model measures the systemic risk the borrower is exposed to.

Furthermore, the Borrower-to-Borrower is constructed via a topological network of borrowers and entities, along with measuring the relationships between them. The entities and relationships are obtained using a domain-expert mathematical model combined with a text-to-entity approach, in which key phrases and topics from the unstructured text are mapped into graph nodes and edges.
We use both on-chain and off-chain data froms borrowers, along with a real-time alert system to update the risk indicators. Finally, our product allocates borrowers into trenched lending pools to ensure that the risk of default of the lending pool as a whole is minimized, while also ensuring that liquidity is available.

## Team ##
**Radu Ciobanu, PhD** (https://www.linkedin.com/in/radu-ciobanu-77aa50177/) has a PhD in Computer Science from University of Edinburgh, did research on graph theory, probabilistic systems and machine learning, worked as a quantitative researcher and former startup CTO of a machine learning for risk management startup (Predictnow.ai - [https://predictnow.ai/](https://predictnow.ai/))

**Flavius Mardare** (https://www.linkedin.com/in/flaviusmardare/) is a Computer Science Grad from University of Birmingham, that’s been in the DeFi space for 5 years. Has grown engineering teams through his past role as a Startup Tech Lead while also having done business deals as a previous founder. 

**Dan Costinescu, PhD** (https://www.linkedin.com/in/dan-n-costinescu-58baa7a/) Financial Advisor @ Invictus Labs & Portfolio Manager @ Andurand Capital

**Roxana Danila** (https://www.linkedin.com/in/roxdanila/) Risk Assessment Advisor @ Invictus Labs & CTO @ Nexus Mutual

**Pandelis Zembashis** (https://www.linkedin.com/in/pandelis/) Technical Advisor @ Invictus Labs & Tech Lead @ Papaya

## Value added to Aave ##
In light of recent events, we’ve seen that the DeFi space is opaque and gated, pushing investors away. The whole ecosystem is hurting from this, including Aave. Through the proposed approach, we strive to help Aave become the leader of both over-collateralized and under-collateralized lending by:

- Bringing into Aave the already existing on-chain Institutional Borrowers while also forming new relationships with off-chain Institutions looking to borrow. Invictus Labs will focus exclusively on Institutional customers as we believe them to be the key to unlocking new levels of DeFi liquidity.
- Bringing trust and transparency to the future Aave under-collateralized Liquidity Pools by measuring Systemic Risk through our systems. This means that we will be able to answer questions such as how the behaviour of a malicious borrower could "intoxicate" others, via ripple effects.
- Vastly increased TVL as a consequence of the new type of borrowers (Trusted Institutions) brought into the ecosystem and the Risk Assessment System presented in the sections to follow.
- Real-time event-driven Alert-System that will keep track of the risk assumed by Aave lenders and allow for more sustainable and stats-drive decisions.

## Proposed Aave Integration ##
In the past few weeks, we've had discussions with different Aave DAO members, including AaveCompanies, to figure out which is the best integration to bring as much value to Aave as fast as possible.
Those discussions conclude with the following proposal:

- The final stages of the integrations will be represented by our system acting as an approved Facilitator for the under-collateralized lending bucket of the $GHO proposal and will derive value through the creation of stable lending liquidity pools curated through our novel risk assessor.
- To get there, we need to gain the trust of the Aave DAO. We plan on doing that by contributing to the DAO with analyses on different lends executed on various Aave Pools and how this will impact the ecosystem as a whole. This alpha will be offered from the beginning, as soon as our MVP is live. Our team is working on that as we speak.
- We are also considering working on getting whitelisted for the Aave Arc Pool, to start the under-collateralised lending process in a more gated environment, before moving on to the final stages with $GHO.

## Further Clarifications ##
The MVP will be a dashboard that the AaveDAO will have complete access to. This dashboard will allow the AaveDAO to check the health (risk metric) of an under-collateralised lending pool using the Systemic Risk algorithm outlined in the Grant Description. Furthermore, the Visualiser component of the dashboard will offer explainability into the measured risk. 

Now, the main question is how we will assess the health of these pools. To answer that, we will measure two things:

1. The probability of default for each individual borrower in the pool.
2. How other entities that these borrowers interact with can negatively impact the financial health of the initial borrowers (those in the Aave pools).

In summary, if our systems had been live a year ago, we claim they would have been able to detect, for example, how the simple loan that Gemini gave to Genesis (an apparently healthy institution) would eventually cause that loan to default, as Genesis was involved in other, riskier ventures.
Systems like these are the standard in making TradFi institutional loans sustainable, but they have not yet been implemented in DeFi.

## 3 Point Methodology for Risk Assessment ##
* Copula model (our benchmark)
* Stand-alone model (also known as Borrower model)
* Graph-based model (also known as Borrower-to-Borrower model)

## Architecture ##
![image-description](assets/borrow_to_borrow_alert.png)




### Data ###

What kind of data do we use and how do we structure it?



- **On-chain data** module: uses (wallet) transaction data on DeXes and metrics from wallet addresses
- **Off-chain data** module: uses balance sheets, margin/leverage history, equity/liquidity,  business registration details, historical business data, payment history and collections, public fillings, etc. Furthermore, we are testing a novel way of tokenisation of future borrower income. This will create the possibility of utilising the tokenised predicted-income as collateral.

- **Data aggregator engine**: will combine the previous 2 modules, and will output structured *entities* and *relationships* between entities. We will use a domain-expert mathematical model, along with a text-to-entity machine learning approach, by  capturing entities and relationships from unstructured text data.

**What if the borrower does not offer sufficient off-chain data?**<br />

For this situation, we have economic incentive mechanisms in place to reward the borrower for data sharing. That is, lack of shared information will lead to a higher risk rating, which will determine the system to make a high interest rate offering. Furthermore, we will also make use of existing APIs that track unstructured text data, such as from Twitter, Discord, etc. to derive the risk level from the captured borrower's behaviour. Lastly, our real-time **Alert System** makes use of existing API market services (such as Bloomberg, Moonpass, Nansen) to track whether a specific event/news will increase/decrease the borrower's risk of default.

### Our Benchmark: Copula model ###

A copula model is a type of mathematical model that is used to describe the dependence between different sources of risk. In the context of credit risk, a copula model can be used to understand the relationship between the likelihood of a borrower defaulting on a loan and the potential impact of that default on the lender, or other borrowers.

The model consists of two components: a *marginal* model, which describes the distribution of the individual sources of risk, and a *copula* function, which describes the dependence between those sources of risk. The marginal model can be specified using a variety of different parametric forms, such as the logistic or normal distributions, while the copula function can also be specified using parametric forms such as the Gaussian or Clayton copulas. 

### Borrower model ###
The stand-alone borrower model is a neural network model trained on the data structured in the **Data Aggregator Engine**, outputting the credit risk of default for a borrower, without taking into account any other systemic risk created by other players in the field. This is used to calculate the **Individual credit risk** (see below). 


### Borrower-to-Borrower model ###
In light of crypto recent events, borrower activities both depend upon and have consequences on the DeFi/Web3 ecosystem. *Knowledge graphs* are able to synthesize different kinds of knowledge and explicitly account for the probabilities of different scenarios, therefore offering a very useful tool for risk assesment. 

In other words, one can answer questions about the probability of the default of a borrower A based on having exposure or a transitive relationship to borrower B.  

As an example, imagine there is a borrower A who is connected to B who gave out a huge loan to C - hence, entity A is connected to B by a relation, while B and C will be connected by another relation. Hence, this dependency may influence borrower A's ability to pay back his loan. 

In order to build the graph model, the **Data Aggregator Engine** will fetch as input what *On-chain* and *Off-Chain* data modules offer, giving as output a tuple under the form *(Entity, Relationship, Entity)*. The on-chain data is more structured, by connecting wallets/pools as entities  and transactions (with their corresponding numerical values) as relationships.
For the off-chain data (such as reports, balance sheets, etc), we will make use of both a domain expert mathematical model and a text-to-entity approach, by identifying entities and relationships. 

We need to quantify the relationships between entities. Hence, every edge in the knowledge graph will have a numerical value that will tell how dependent an entity is to another entity. 
Rather than spanning out a very large number of edges, we need to abstract out from them, by combining multiple relations that an entity A may have with entity B into a single one, with a corresponding risk impact. In other words, **not all relationships matter equally in terms of importance.** 

**The most important thing is to measure the relations between entities, and how this affects the risk metric. We will make use of a Bayesian network to achieve that.**

**Bayesian networks** (causal inference models) are a type of probabilistic graphical model that explicitly describe
dependencies between a set of variables using a directed acyclic graph (DAG) and a set of
node probability tables (NPTs). Each node in a DAG has a node probability table (NPT) which describes the probability
distribution of the node conditional on its parents.

Then, based on the specific factors, such as exposure, loans, team being implied into a bad activity, etc, we will update the risk impact on the knowledge graph edges. 







## Risk assesment methodology ##

For every borrower, we will construct a **Overall Risk Score** which is composed of the output of the model trained on the data offered by the borrower/ any externally accessibile data sources (**Individual credit risk**), along with the output of the knowledge graph inference model based on its relation with other borrowers (**Systemic Credit Risk**). See below:

**Individual Credit Risk** - i.e., risk of default of a borrower considered as a **stand-alone entity**.  It is obtained via assessing the risk of default obtained from the Borrower model (based on the data provided via the *Data Aggregator Engine*).

**Systemic Credit Risk** - obtained from the output of the Borrower-to-Borrower model, which will determine what is the risk of default if existing exposure to another borrower or external entities.

The **Overall risk score** of a borrower is a weighted average between *Individual Credit Risk* and *Systemic Credit Risk*, with the exact weights to be determined via experiments, or as a dynamic weighting mechanism, based on market regime. 



## Allocation Engine ##
The **Allocation Engine** constructs a diversified "portfolio" of borrowers allocated to specific pools given different constraints, such as the overall lending pool risk is minimized, available liquidity exists, etc. We will make use of state of the art portfolio allocation algorithms from Hudson and Thames to speed up the allocation process.






