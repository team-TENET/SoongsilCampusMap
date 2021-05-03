package com.example.bottomnavitest.view;

import android.content.Context;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import androidx.fragment.app.Fragment;

import com.example.bottomnavitest.R;
import com.example.bottomnavitest.model.Post;
import com.example.bottomnavitest.service.PostService;

public class Frag4 extends Fragment {
    private View view;
    private Context context;
    //객체선언
    EditText ed_title;
    EditText ed_subject;
    TextView ed_result;
    Button btnSend;

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container, @Nullable Bundle savedInstanceState) {
        //선언한 객체를 onCreateView에 보여주게 함.
        view = inflater.inflate(R.layout.frag2, container, false);
        btnSend = (Button)view.findViewById(R.id.btn_sendData);
        ed_title = (EditText)view.findViewById(R.id.et_message);
        ed_subject = (EditText)view.findViewById(R.id.et_message);
        ed_result = (TextView)view.findViewById(R.id.tv_recvData);

        btnSend.setOnClickListener(this::onClick);
        context = container.getContext();
        return view;
    }

    public void onClick(View v){
        //눌렀을때 가정.
        switch(v.getId()){

            //버튼 클릭 시.
            case R.id.btn_sendData:
            {
                //Edittext를 String으로 변환해서 Toast하게 함.
                String title = ed_title.getText().toString();
                String subject = ed_subject.getText().toString();
                Toast.makeText(context, title, Toast.LENGTH_SHORT).show();
                ed_result.setText(subject);
                //일단 테스트중. 서버접속해서 보내는거까지 하고싶음.
                String sentresult = PostService.writePost("http://127.0.0.1:8080/boards/1/posts", new Post(1, title, subject));
                Toast.makeText(context, sentresult, Toast.LENGTH_SHORT).show();

            }
        }
    }
}
