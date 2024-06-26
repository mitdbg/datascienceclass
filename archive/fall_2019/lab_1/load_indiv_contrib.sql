.mode csv
.separator |
DROP TABLE IF EXISTS indiv_contrib;
CREATE TABLE indiv_contrib(
  "CMTE_ID" VARCHAR(9),
  "AMNDT_IND" VARCHAR(1),
  "RPT_TP" VARCHAR(3),
  "TRANSACTION_PGI" VARCHAR(5),
  "IMAGE_NUM" VARCHAR(18),
  "TRANSACTION_TP" VARCHAR(3),
  "ENTITY_TP" VARCHAR(3),
  "NAME" VARCHAR(200),
  "CITY" VARCHAR(30),
  "STATE" VARCHAR(2),
  "ZIP_CODE" VARCHAR(9),
  "EMPLOYER" VARCHAR(38),
  "OCCUPATION" VARCHAR(38),
  "TRANSACTION_DT" DATE,
  "TRANSACTION_AMT" FLOAT,
  "OTHER_ID" VARCHAR(9),
  "TRAN_ID" VARCHAR(32),
  "FILE_NUM" INT,
  "MEMO_CD" VARCHAR(1),
  "MEMO_TEXT" VARCHAR(100),
  "SUB_ID" VARCHAR(19)
);
.import data/itcont.txt indiv_contrib
