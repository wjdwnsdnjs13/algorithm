class Solution {
        int time;
        int videoLen;
        int opStart;
        int opEnd;
    
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        // video_len : 동영상 길이
        // pos : 재생 위치
        // op_start : 오프닝 시작 시간
        // op_end : 오프닝 끝 시간
        // commands : 사용자의 커맨드
        
        // prev : 10초 전 이동
        // next : 10초 후 이동
        // 자동 : 오프닝 건너 뛰기
        
        // int로 전부 바꿔서 맨 마지막에 mm:ss로 바꾸기
        time = timeToInt(pos);
        videoLen = timeToInt(video_len);
        opStart = timeToInt(op_start);
        opEnd = timeToInt(op_end);
        
        
        time = skipFunc(time);
        for(String command: commands){
            if(command.equals("prev")) time = prevFunc(time);
            else if(command.equals("next")) time = nextFunc(time);
            time = skipFunc(time);
        }
        return intToTime(time);
    }
    
    public int timeToInt(String t){
        return ((t.charAt(0) - '0') * 10 + (t.charAt(1) - '0')) * 60 + (t.charAt(3) - '0') * 10 + (t.charAt(4) - '0');
    }
    
    public String intToTime(int t){
        String m = String.valueOf(t/60);
        String s = String.valueOf(t%60);
        
        if(m.length() == 1) m = "0" + m;
        if(s.length() == 1) s = "0" + s;
        return m + ":" + s;
    }
    
    public int prevFunc(int t){
        return (t - 10 > 0)?(t - 10):0;
    }
    
    public int nextFunc(int t){
        return (t + 10 < videoLen)?(t + 10):videoLen;
    }
    
    public int skipFunc(int t){
        if(t >= opStart && t <= opEnd) return opEnd;
        return t;
    }
}