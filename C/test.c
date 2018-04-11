#include <stdio.h>

//这里因为C语言限制，在函数内一般大于1000列以上的数组会报错，所以写到主函数外作为全局变量，这个可以自己算好
//原始矩阵Matrix
int Matrix[2464][2464];
//拆分后的矩阵合集（共1936个）little_matrix
int little_matrix[1936][56][56];

void main(){
    //初始化矩阵
    int v = 1;
    int i, j;
    for (i=0;i<2464;i++){
        for (j=0;j<2464;j++){
            Matrix[i][j] = v;
                v++;
        }
    }

    // //获取拆分个数,并创建三维数据
    int little_matrix_row = (2464 / 56);
    int little_matrix_num = little_matrix_row * little_matrix_row;
    printf("%d\n", little_matrix_num);

    //四次循环
    //l_m_no为little_matrix矩阵标号
    //l_r_no为该子矩阵的行号，l_r_no为该子矩阵的列号
    int l_m_no=0,l_r_no, l_c_no, m, n;
    for (l_r_no=0;l_r_no<little_matrix_row;l_r_no++) {
        for (l_c_no=0;l_c_no<little_matrix_row;l_c_no++){
            //printf("%d-%d-%d\n",l_m_no, l_r_no, l_c_no);
            //对应赋值，这里可以自己试下逻辑，不好说
            for (m=0;m<56;m++){
                for (n=0;n<56;n++){
                    int m_i = 56*l_r_no + m;
                    int m_j = 56*l_c_no + n;
                    little_matrix[l_m_no][m][n] = Matrix[m_i][m_j];
                }
            }
            l_m_no++;
        }
    }

    int tt;
    //输出每个子矩阵的最后一个元素
    for (tt=0;tt<little_matrix_num; tt++){
        printf("%d\n", little_matrix[tt][55][55]);
    }
    
}

