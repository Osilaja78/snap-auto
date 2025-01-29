/*
 * Copyright (C) 2024 The Android Open Source Project
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */
package com.android.internal.widget.remotecompose.core.operations;

import com.android.internal.widget.remotecompose.core.CompanionOperation;
import com.android.internal.widget.remotecompose.core.Operation;
import com.android.internal.widget.remotecompose.core.Operations;
import com.android.internal.widget.remotecompose.core.PaintContext;
import com.android.internal.widget.remotecompose.core.PaintOperation;
import com.android.internal.widget.remotecompose.core.WireBuffer;

import java.util.List;

public class DrawLine extends PaintOperation {
    public static final Companion COMPANION = new Companion();
    float mX1;
    float mY1;
    float mX2;
    float mY2;

    public DrawLine(
            float x1,
            float y1,
            float x2,
            float y2) {
        mX1 = x1;
        mY1 = y1;
        mX2 = x2;
        mY2 = y2;
    }

    @Override
    public void write(WireBuffer buffer) {
        COMPANION.apply(buffer, mX1,
                mY1,
                mX2,
                mY2);
    }

    @Override
    public String toString() {
        return "DrawArc " + mX1 + " " + mY1
                + " " + mX2 + " " + mY2 + ";";
    }

    public static class Companion implements CompanionOperation {
        private Companion() {
        }

        @Override
        public void read(WireBuffer buffer, List<Operation> operations) {
            float x1 = buffer.readFloat();
            float y1 = buffer.readFloat();
            float x2 = buffer.readFloat();
            float y2 = buffer.readFloat();

            DrawLine op = new DrawLine(x1, y1, x2, y2);
            operations.add(op);
        }

        @Override
        public String name() {
            return "DrawLine";
        }

        @Override
        public int id() {
            return Operations.DRAW_LINE;
        }

        public void apply(WireBuffer buffer,
                          float x1,
                          float y1,
                          float x2,
                          float y2) {
            buffer.start(Operations.DRAW_LINE);
            buffer.writeFloat(x1);
            buffer.writeFloat(y1);
            buffer.writeFloat(x2);
            buffer.writeFloat(y2);
        }
    }

    @Override
    public void paint(PaintContext context) {
        context.drawLine(mX1,
                mY1,
                mX2,
                mY2);
    }

}
