import unittest  # Тест үүсгэж, ажиллуулахад зориулсан unittest модулийг импортолж байна.

# Хайлтын хамгийн бага өртгийг тооцох функц
def min_search_cost(n, k, f):
    # Давтамжийн жагсаалтыг ихээс бага руу эрэмбэлж, өндөр давтамжийг түрүүлж тооцоолох
    sorted_f = sorted(f, reverse=True)
    
    # Түлхүүрийн жагсаалтыг багаас их рүү эрэмбэлж, бага өртөгтэй түлхүүрүүдэд өндөр давтамж өгч тааруулах
    sorted_k = sorted(k)
    
    # Нийт хайлтын өртгийг хадгалах total_cost хувьсагчийг эхлүүлнэ
    total_cost = 0
     # Жагсаалтын элемент бүрийг давтаж, жингийн өртгийг тооцох
    for i in range(n):
        # Давтамжийг түүний жингийн байрлалтай үржүүлж, нийт өртөгт нэмнэ
        total_cost += sorted_f[i] * (i + 1)
    return total_cost
class TestMinSearchCost(unittest.TestCase):
    def test_case_1(self):
        n = 2   
        k = [5, 6]  
        f = [17, 25] 
        result = min_search_cost(n, k, f)
        self.assertEqual(result, 59)  
if __name__ == '__main__':
    unittest.main()
