import java.util.HashMap;



public class HashMapPra
{
    public static void main(String[] args)
    {
        HashMap<String , Integer> map = new HashMap<>();

        map.put("key1" , 10);
        map.put("key2" , 20);
        map.put("key3" , 30);

        System.out.println("Size of map is : " + map.size());
        System.out.println(map);

        if (map.containsKey("key2")){    // getting value of key
            Integer a = map.get("key2");

            System.out.println("Value of key2 :" + a);

            System.out.println(map.values());
            System.out.println(map.keySet());

            map.forEach((key, value) -> {
                System.out.println(key + value);
            });

            
        }
    }
}