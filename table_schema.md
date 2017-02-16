# table schema:
### **InstanceId**
+ 创建表：
    
    create table InstanceId(Ins binary varchar(255) not null , Id int not null);
    --均未使用主键，而是后面直接创建索引，使用主键会降低插入速度,binary代表大小写敏感
    
+ 创建索引：

        
    create index indexInstance on InstanceId(Ins);
    --创建Instance的索引
    create index indexId on InstanceId(Id);
    --创建Id的索引
        
+ desc InstanceId:


### **PredicateId**
+ 创建表：


    create table PredicaetId(Pred binary varchar(255) not null , Id int not null);
    --均未使用主键，而是后面直接创建索引，使用主键会降低插入速度,binary代表大小写敏感
    --然而这个我还是在Id上创建了primary key，不过这个表小，影响不大，至少目前影响不大
    
+ 创建索引：

        
    create index indexPredicate on PredicateId(Pred);
    --创建Predicate的索引
    create index indexPredicateId on PredicateId(Id);
    --创建Id的索引
        
+ desc PredicateId:

 Field | Type         | Null | Key | Default | Extra |
-------|--------------|------|-----|---------|-------|
 Pred  | varchar(255) | YES  | MUL | NULL    |       |
 id    | int(11)      | NO   | PRI | NULL    |       |


### **S_OP**
+ 创建表：


    create table S_OP(Sub int not null , ObjPred varchar(255) not null);
    --均未使用主键，而是后面直接创建索引，使用主键会降低插入速度,
    
+ 创建索引：

        
    create index indexSub on S_OP(Sub);
    --创建Sub的索引
    create index indexObjPred on S_OP(ObjPred);
    --创建ObjPred的索引
        
+ desc S_OP:

 Field   | Type         | Null | Key | Default | Extra 
---------|--------------|------|-----|---------|-------
 Sub     | int(11)      | NO   | MUL | NULL    |       
 ObjPred | varchar(255) | YES  | MUL | NULL    |       
 

### **O_SP**
+ 创建表：


    create table O_SP(Obj int not null , SubPred varchar(255) not null);
    --均未使用主键，而是后面直接创建索引，使用主键会降低插入速度,
    
+ 创建索引：

        
    create index indexObj on O_SP(Obj);
    --创建Obj的索引
    create index indexSubPred on O_SP(SubPred);
    --创建SubPred的索引
        
+ desc O_SP:

 Field   | Type         | Null | Key | Default | Extra 
---------|--------------|------|-----|---------|-------
 Obj     | int(11)      | NO   | MUL | NULL    |       
 SubPred | varchar(255) | NO   | MUL | NULL    |        


### **P_SO**
+ 创建表：


    create table P_SO(Pred int not null , SubObj varchar(255) not null);
    --均未使用主键，而是后面直接创建索引，使用主键会降低插入速度,
    
+ 创建索引：

        
    create index indexPred on P_SO(Pred);
    --创建Pred的索引
    create index indexSubObj on P_SO(SubObj);
    --创建SubObj的索引
        
+ desc P_SO:

 Field  | Type         | Null | Key | Default | Extra 
--------|--------------|------|-----|---------|-------
 Pred   | int(11)      | NO   | MUL | NULL    |       
 SubObj | varchar(255) | NO   | MUL | NULL    |       
 
