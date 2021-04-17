package com.example.bottomnavitest.service;

import android.util.Log;

import com.example.bottomnavitest.model.Post;

import org.json.JSONObject;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;

import lombok.RequiredArgsConstructor;


@RequiredArgsConstructor
public class PostService {
    public static String writePost(String url, Post post) {
        InputStream is = null;
        String result = "";
        String json="";
        try{
            java.net.URL urlCon = new URL(url);
            HttpURLConnection httpCon = (HttpURLConnection)urlCon.openConnection();
            Post post2 = new Post();
            //JSON Build
            JSONObject jsonTest = new JSONObject();
            jsonTest.accumulate("userId", post.getUserId());
            jsonTest.accumulate("title", post.getTitle());
            jsonTest.accumulate("subject", post.getSubject());

            json = jsonTest.toString();

            httpCon.setRequestProperty("Accept", "application/json");
            httpCon.setRequestProperty("Content-type", "application/json");
            // OutputStream으로 POST 데이터를 넘겨주겠다는 옵션.
            httpCon.setDoOutput(true);
            // InputStream으로 서버로 부터 응답을 받겠다는 옵션.
            httpCon.setDoInput(true);

            OutputStream os = httpCon.getOutputStream();
            os.write(json.getBytes("euc-kr"));
            os.flush();
            // receive response as inputStream
            try {
                is = httpCon.getInputStream();
                // convert inputstream to string
                if(is != null) {
                    result = "Worked!";
                    //result = convertInputStreamToString(is);
                }
                else
                    result = "Did not work!";
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            finally {
                httpCon.disconnect();
            }
        }
        catch (IOException e) {
        e.printStackTrace();
        }
        catch (Exception e) {
        Log.d("InputStream", e.getLocalizedMessage());
        }
        return result;
    }

    public Post getPost(int postId){
        Post post = new Post();
        return post;
    }
}
