package Java;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class Task_Java {
//     1. Осуществить подсчет слов:
// Напишите программу, которая подсчитывает количество слов в
// файле `input.txt`.
// 2. Найти самое длинное слово:
// Создайте программу, которая находит самое длинное слово в
// файле.
// 3. Вычислить частоту слов:
// Напишите программу, которая анализирует, сколько раз каждое
// слово встречается в файле. Подумайте об этом как о подсчете того,
// какие фрукты и овощи самые популярные на вашем пикнике! 

    public static void main(String[] args) {
        String fileName = "Java\\input.txt";

        // Осуществить подсчет слов
        countWords(fileName);
        
        // Найти самое длинное слово
        findLongestWord(fileName);
        
        // Вычислить частоту слов
        calculateWordFrequency(fileName);
    }

    public static void countWords(String fileName) {
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            int wordCount = 0;
            while ((line = br.readLine()) != null) {
                wordCount += line.split(" ").length;
            }
            System.out.println("Количество слов в файле: " + wordCount);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void findLongestWord(String fileName) {
        try (BufferedReader br = new BufferedReader(new FileReader(fileName)) ){
            String line;
            String longestWord = "";
            while ((line = br.readLine()) != null) {
                String[] words = line.split(" ");
                for (String word : words) {
                    if (word.length() > longestWord.length()) {
                        longestWord = word;
                    }
                }                
            }
            System.out.println("Самое длинное слово в файле: " + longestWord);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void calculateWordFrequency(String fileName) {
        Map<String, Integer> wordFrequency = new HashMap<>();
        try (BufferedReader br = new BufferedReader(new FileReader(fileName))) {
            String line;
            while ((line = br.readLine()) != null) {
                String[] words = line.split(" ");
                for (String word : words) {
                    wordFrequency.put(word, wordFrequency.getOrDefault(word, 0) + 1);
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println("Частота слов в файле: " + wordFrequency);
    }
}