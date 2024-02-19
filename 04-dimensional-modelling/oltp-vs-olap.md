### OLTP vs OLAP

---

#### Transactional Databases (OLTP)

Initially, a write to a database corresponded to a commercial transaction - any activity that supports company to customer-direct trading activity e.g a customer purchasing a product at a POS, placing an order with a supplier, paying an employees salary. The word transaction has since evolved to mean a group of logical reads and writes that forms a logical unit.

The access pattern of transactional databases entails real time or near-real time, small transactions that is written to a database. Transactional databases are optimized for small, concurrent *INSERTS, UPDATES and DELETES* . For example, say a supermarket chain has multiple customers making purchases. The transactions have to be fast (*low latency*, and the data being written is small.

Transactional databases support business processes, they form the backend of  application software. 

### Analytical Databases (OLAP)

As database requirements evolved, they begun to be used for analytics. OLAP databases are meant to help inform management to make decisions. Decision support databases provides reports, via analytical queries, such as the total  inventory of a product, or quantity of products sold over a year or the first quarter.

OLAP have a different access pattern in contrast to OLTP. Whereas OLTP is optimized small, fast and concurrent transactions, OLAP is optimized for large analytical reporting requirements. This is accessed in the form of batch jobs.

#### The Hardware problem

In the 80s, and early 90s, transactions and analytics were handled in the same database. This presented some problems that subsequently led to the development of the data warehouse.

> "Operational databases need highly efficient sharing of critical resources such as onboard memoery (RAM), and have small I/O requirements. Data warehouses are completely opposite. They consume large portions of RAM by transferring data between disk and memory, in detriment to an OLTP database running on on the same machine. Whereas OLTP databases need resource sharing, data warehouses need to hog those resources for extended periods of time. A data warehouse hogs machine resources, an OLTP attempts to share those resources, it is likely to have an unacceptable response time due to lack of basic I\O resources for both database types."

#### Difference OLTP and OLAP

| Property              | OLTP                                                             | OLAP                                              |
| --------------------- | ---------------------------------------------------------------- | ------------------------------------------------- |
| main read pattern     | Small number of records per query, fetched by key.               | Aggregate over a large number of records.         |
| main write pattern    | random-access, low-latency writes from user input.               | Bulk import ETL or event stream.                  |
| primary users         | End user/customer via a web application.                         | Business or data analyst, for decision support.   |
| Dataset size          | GB to TB                                                         | TB to PB                                          |
| hardware requirements | require intensely shareable hardware structures for concurrency. | large amounts of disk space and processing power. |
| optimzation           | optimized for INSERTS, UPDATES  and WRITES                       | optimized for READS                               |

#### Recommended Resources

NOTE : These can be found in the Google Drive link

1. *Designing Data Intensive Applications - Martin Kleppman* , Chapter 3. Storage and Retrieval

2. *The DataWarehouse Toolkit - Ralph Kimball*  ,Chapter 1

3. *Beginning Database Design - Gavin Powell* ,Chapter 7. Understanding Data Warehouse Database Modelling

4. *Deciphering Data Architectures - James Serra* ,Chapter 2. Types of Data Architectures
